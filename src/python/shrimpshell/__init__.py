#!/usr/bin/python

import sys,os,copy,threading,traceback,argparse,glob,pdb

from time import sleep,time
from threading import Thread
from string import Formatter
from watchdog.observers import Observer

class Runner(object):
    
    def __init__(self,  description='Search recursively from a root for input files'+
                        'matching a specific pattern, run a command'+
                        'on that file. Allows for rich substitution'+
                        'syntax based on python\'s str.format, '+
                        'by both console args and contextual args '+
                        'derived from the matched input files'):
        self.parser = argparse.ArgumentParser(description)
        self.initparser(self.parser)

    def initparser(self, parser):
        parser.add_argument('--workingdirectory',
            default='.{sep}', # default is the current directory
            help='The root directory to which this python script will'+
            'change, before recursively searching for input files'
        )
        parser.add_argument('--inputfileglob',
            default='*.md',
            help='The filename pattern (glob) searched recursively from'+
                    '{workingdirectory} for files to process'
        )
        parser.add_argument('--inputpathglob',
            default='{parentpath}{sep}{inputfileglob}',
            help='The filename pattern (glob) searched recursively from'+
                    '{workingdirectory} for files to process'
        )
        parser.add_argument('--outputdirname', default='.{sep}',
            help='The pattern to use to generate the output directory'+
                'relative to the {workingdirectory}'
        )
        parser.add_argument('--outputfiletemplate', default='{outputdirname}{sep}{inputbasename}.out',
            help='The pattern to use to generate the output file'+
            '{vars} value for the {shellcmd} substitution, relative to the {workingdirectory}'
        )
        parser.add_argument('--var',
            nargs=2,
            action='append',
            help='A single entry used to populate the {varstring} value '+
                    'available to the {shellcmd} substitution'
        )
        parser.add_argument('--varpattern', 
            default='-v {name} {value} ', # intended for xqilla
            help='The str.format to use for each variable when generating the '+
                    '{varstring} value for the {shellcmd} substitution'
        )
        parser.add_argument('--shellcmd',
            default='echo "No shellcmd specified, so echoing: {inputpath}"',
            help='A str.format for the shell command to run when an input'+
                    'file change is detected, or when updated output is '+
                    'forced'
        )
        parser.add_argument('--burstwindow', 
            default=-1,
            help='If specified, events separated by less than this '+
                'delay are treated as a single event, with a single'+
                'refresh called at the end of the burst (assuming the '+
                'burst comes to an end'
        )
        parser.add_argument('--norun',
            action='store_true',
            help='Controls whether all command lines for matched files '+
            'are run once immediately on launch'
        )
        parser.add_argument('--watch',
            action='store_true',
            help='Controls whether the utility should block waiting '+
                'for updates to the matched files, and re-run commands'
        )
        parser.add_argument('--watchextra',
            action='append',
            help='Specify extra paths to monitor with this argument'
        )

    @property
    def rundict(self):
        try:
            return self._rundict
        except:
            args = self.parser.parse_args()
    
            self._rundict = ResolvingDict(**vars(args))
            
            # make os filesystem separator available
            self._rundict['sep'] = os.sep

            # could be generalised?
            # populate from '--var {name} {value}' command line entries
            self._rundict['varstring'] =''
            
            if args.var != None:
                for item in args.var:
                    self._rundict['varstring'] += str.format(args.varpattern, **{name:item[0],value:item[1]})

            self._rundict['inputpaths'] = self.inputpaths

            return self._rundict
    
    @property
    def inputpaths(self):

        # change to the specified working directory
        os.chdir(self.rundict['workingdirectory'])

        try:
            return self._inputpaths
        except:
            self._inputpaths = []
            for parentpath, dirpaths, filepaths in os.walk('.'):
                parentdict = ResolvingDict(**self.rundict)
                parentdict['parentpath'] = parentpath
                self._inputpaths += glob.glob(parentdict['inputpathglob'])
            return self._inputpaths

    def execute(self):

        # change to the specified working directory
        os.chdir(self.rundict['workingdirectory'])

        if not self.rundict['norun']:
            self.runallcommands()

        if self.rundict['watch']:
            self.observer = Observer()
            handler = Watcher(self,self.rundict['burstwindow'])
            watchpaths = [self.rundict['workingdirectory']]
            try:
                watchpaths.extend(self.rundict['watchextra'])
            except:
                pass # watchextra not provided
            for watchpath in watchpaths:
                if not os.path.isdir(watchpath):
                    watchpath = os.path.dirname(watchpath)
                self.observer.schedule(handler, watchpath, recursive=True)
            self.observer.start()
            try:
                while True:
                    sleep(1)
            except KeyboardInterrupt:
                self.observer.stop()
                self.observer.join()


    def runallcommands(self):

        # process all paths
        for inputpath in self.inputpaths:
            # populate values specific to this input file
            inputdict = ResolvingDict(**self.rundict)
            inputdict['inputpath'] = inputpath # the path to the file
            inputdict['inputdirname'] = os.path.dirname(inputpath) # the directory holding the file
            inputdict['inputbasename'] = os.path.splitext(os.path.basename(inputpath))[0] # unix 'basename' without extension not python basename
            self.runcommand(inputdict)


class Watcher(object):
    
    def __init__(self, runner, burstwindow):
        self.runner = runner
        self.burstwindow = float(burstwindow)
        self.burstthread = None

    def dispatch(self, event): # watchdog call for any filesystem event
        self.lasteventtime = time()
        if self.burstthread == None:
            self.burstthread = Thread(target=self.runafterburst)
            self.burstthread.start()

    def runafterburst(self):
        while True: # wait until last event older than burstwindow
            duetime = self.lasteventtime + self.burstwindow
            waittime = duetime - time() 
            if waittime < 0:
                break
            else:
                sleep(waittime)
                
        if threading.current_thread() == self.burstthread:
            self.burstthread = None
            self.runner.runallcommands()

# A subclass of python's native dict, which auto-populates values with
# template strings like {key} by looking up other string values stored
# within the dict
class ResolvingDict(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        self.resolvedstrings = dict()

    # recursively expands string values using str.format, drawing from
    # its own dict entries and eliminating circular references by
    # checking against a thread-local list of references which are on
    # the 'resolving stack' - note this does not work when Formatter
    # class vformat call is substituted with (ostensibly equivalent)
    # str.format call
    def __getitem__(self, key):
        val = dict.__getitem__(self, key)
        #print("GET %s['%s'] = %s" % str(dict.get(self, 'name_label')), str(key), str(val))
        if type(val) is str:
            if key not in self.resolvedstrings:
                try:
                    # used to track circular refs
                    threadlocal = threading.local()
                    
                    try: # check if resolution list already allocated
                        threadlocal.resolving 
                        allocatedhere = False 
                    except: # resolution list not already allocated
                        threadlocal.resolving = list()
                        allocatedhere = True
                        
                    # quit on circular refs
                    if key in threadlocal.resolving:
                        raise Error('Cycle found in references! ' + threadlocal.resolving )
                    else:                    
                        # recursively expand string value with string.Formatter
                        threadlocal.resolving.append(key)
                        self.resolvedstrings[key]=Formatter().vformat(val,[],self)
                        threadlocal.resolving.pop()
                finally:
                    if allocatedhere : # de-allocate resolution list
                        del threadlocal.resolving
                        
            return self.resolvedstrings[key]
        else:
            return val


if __name__ == "__main__":
    runner = Runner()
    runner.run()