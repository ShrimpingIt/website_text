#!/usr/bin/python

import sys,os,copy,subprocess,threading,traceback,argparse,glob,pdb

from string import Formatter
from watchdog.observers import Observer

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

class Runner(object):
    
    def __init__(self):
        
        self.parser = argparse.ArgumentParser(
            description='Search recursively from a root for input files'+
                            'matching a specific pattern, run a command'+
                            'on that file. Allows for rich substitution'+
                            'syntax based on python\'s str.format, '+
                            'by both console args and contextual args '+
                            'derived from the matched input files'
        )
        self.parser.add_argument('--rootdir',
            default='.{sep}', # default is the current directory
            help='The root directory from which to recursively search files'
        )
        self.parser.add_argument('--inputfileglob',
            default='*.md',
            help='The filename pattern (glob) searched recursively from'+
                    '{rootdir} for files to process'
        )
        self.parser.add_argument('--outputfiletemplate', default='../../build/raw/{inputdirname}{sep}{inputbasename}.html',
            help='The pattern to use to generate the output file'+
            '{vars} value for the {shellcmd} substitution'
        )
        self.parser.add_argument('--descendantglob', default='{parentpath}{sep}{inputfileglob}',
            help='The pattern to use to generate the output file'+
                    '{vars} value for the {shellcmd} substitution'
        )
        self.parser.add_argument('--xquery',
            default='{rootdir}..{sep}xquery{sep}index.xq',
            help='A str.format defining the path to an XQuery filter'
        )
        self.parser.add_argument('--var',
            nargs=2,
            action='append',
            help='A single entry used to populate the {varstring} value '+
                    'available to the {shellcmd} substitution'
        )
        self.parser.add_argument('--varpattern', 
            default='-v {name} {value} ', # intended for xqilla
            help='The str.format to use for each variable when generating the '+
                    '{varstring} value for the {shellcmd} substitution'
        )
        self.parser.add_argument('--shellcmd',
            default='echo {inputpath}; mkdir -p $(dirname {outputfiletemplate}); pandoc --from=markdown_github --to=html --standalone {inputpath} '+
                    '|sed 1d '+
                    '|xqilla -i /dev/stdin {xquery} -v serverroot {rootdir} {varstring} '+
                    '> {outputfiletemplate}',
            help='A str.format for the shell command to run when an input'+
                    'file change is detected, or when updated output is '+
                    'forced'
        )

    
    def run(self):

        self.args = self.parser.parse_args()

        rundict = ResolvingDict(**vars(self.args))
        
        # make os filesystem separator available
        rundict['sep'] = os.sep
                    
        # identify matching input files
        inputpaths = []
        for parentpath, dirpaths, filepaths in os.walk(rundict['rootdir']):
            childdict = ResolvingDict(**rundict)
            childdict['parentpath']=parentpath
            inputpaths += glob.glob(childdict['descendantglob'])
        rundict['inputpaths'] = inputpaths
    
        # populate with variables passed in to command line        
        varstring = ''
        if self.args.var != None:
            for item in self.args.var:
                varformatdict = dict()
                varformatdict['name'],varformatdict['value']= item
                varstring += str.format(self.args.varpattern, **varformatdict)
        rundict['varstring'] = varstring
        
        # TODO CH look into generalising the hard-coded varpattern 
        # e.g. look for a *template argument for every 'append'
        # argument, and generate a pluralized argument
        # also should it do this on a per-input basis? should probably
        # use formatdict below somehow, although how to pass the
        # sequential parameters? could be as numerical keys?
        
        # populate and execute shellcmd for each matching input file
        for inputpath in inputpaths:
            
            #dictionary which auto-expands str.format references on access
            inputdict = ResolvingDict(**rundict)            
                        
            # populate values specific to this input file
            inputdict['inputpath'] = inputpath # the path to the file
            inputdict['inputdirname'] = os.path.dirname(inputpath) # the directory holding the file
            inputdict['inputbasename'] = os.path.splitext(os.path.basename(inputpath))[0] # unix 'basename' without extension not python basename
                        
            self.processinput(inputdict)
        
    
    def processinput(self, inputdict):
        #print( inputdict['shellcmd'] )
        subprocess.call(inputdict['shellcmd'],shell=True)

if __name__ == "__main__":
    runner = Runner()
    runner.run()