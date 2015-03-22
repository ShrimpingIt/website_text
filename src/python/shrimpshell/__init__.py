#!/usr/bin/python

import sys,os,copy,threading,traceback,argparse,glob,pdb

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
        parser.add_argument('--outputfiletemplate', default='{inputdirname}{sep}{inputbasename}.out',
            help='The pattern to use to generate the output file'+
            '{vars} value for the {shellcmd} substitution, relative to the {workingdirectory}'
        )
        parser.add_argument('--descendantglob', default='{parentpath}{sep}{inputfileglob}',
            help='The pattern to use to generate the output file'+
                    '{vars} value for the {shellcmd} substitution'
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

    
    def run(self):
        
        args = self.parser.parse_args()

        rundict = ResolvingDict(**vars(args))
        
        # make os filesystem separator available
        rundict['sep'] = os.sep
        
        # change to the specified working directory
        os.chdir(rundict['workingdirectory'])

        # TODO CH look into generalising the hard-coded varpattern 
        # e.g. look for a *template argument for every 'append'
        # argument, and generate a pluralized argument
        # also should it do this on a per-input basis? should probably
        # use formatdict below somehow, although how to pass the
        # sequential parameters? could be as numerical keys?

        # populate from '--var {name} {value}' command line entries
        rundict['varstring'] =''
        if args.var != None:
            for item in args.var:
                rundict['varstring'] += str.format(args.varpattern, **{name:item[0],value:item[1]})
                
                            
        for parentpath, dirpaths, filepaths in os.walk('.'):
            parentdict = ResolvingDict(**rundict)
            parentdict['parentpath'] = parentpath
            for inputpath in glob.glob(parentdict['inputpathglob']):
                inputdict = ResolvingDict(**parentdict) 
                # populate values specific to this input file
                inputdict['inputpath'] = inputpath # the path to the file
                inputdict['inputdirname'] = os.path.dirname(inputpath) # the directory holding the file
                inputdict['inputbasename'] = os.path.splitext(os.path.basename(inputpath))[0] # unix 'basename' without extension not python basename
                self.processinput(inputdict)
    
    def processinput(self, inputdict):
        raise Error('Runner must override processinput')


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