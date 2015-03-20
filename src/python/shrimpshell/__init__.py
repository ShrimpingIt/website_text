#!/usr/bin/python

import sys,os,copy,subprocess,threading,traceback,argparse,glob,pdb

from string import Formatter
from watchdog.observers import Observer

# A subclass of python's native dict, which auto-populates values with
# template strings like {key} by looking up other string values stored
# within the dict
class ResolvingDict(dict):
    def __init__(self, *args):
        dict.__init__(self, args)
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
            default='.', # default is the current directory
            help='The root directory from which to recursively search files'
        )
        self.parser.add_argument('--inputfilematch',
            default='*.md',
            help='The filename pattern (glob) searched recursively from'+
                    '{rootdir} for files to process'
        )
        self.parser.add_argument('--outputfiletemplate', default='{inputdirname}'+os.sep+'{inputbasename}.html',
            help='The pattern to use to generate the output file'+
                    '{vars} value for the {shellcmd} substitution'
        )
        self.parser.add_argument('--xquery',
            default='{rootdir}' + os.sep + 'index.xq',
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
            default='echo {inputpath};pandoc --from=markdown_github --to=html --standalone {inputpath} '+
                    '|sed 1d '+
                    '|xqilla -i /dev/stdin {xquery} -v serverroot {rootdir} {varstring} '+
                    '> {outputfiletemplate}',
            help='A str.format for the shell command to run when an input'+
                    'file change is detected, or when updated output is '+
                    'forced'
        )

        self.args = parser.parse_args()
        
    
    def run(self):
                
        inputpaths = []
        for parent, childdirs, childfiles in os.walk(self.args.rootdir):
            for childdir in childdirs:
               grandchildmatch = parent + os.sep + childdir + os.sep + self.args.inputfilematch
               inputpaths += glob.glob(grandchildmatch)
    
        # populate variables passed in to command line        
        varstring = ''
        if self.args.var != None:
            for item in self.args.var:
                varformatdict = dict()
                varformatdict['name'],varformatdict['value']= item
                varstring += str.format(args.varpattern, **varformatdict) 

        # TODO CH generalise the hard-coded varpattern approach above
        # e.g. look for a *template argument for every 'append'
        # argument, and generate a pluralized argument
        # also should it do this on a per-input basis? should probably
        # use formatdict below somehow, although how to pass the
        # sequential parameters? could be as numerical keys?
        
        # populate and execute shellcmd for each input file
        for inputpath in inputpaths:
            
            #dictionary which auto-expands str.format references on access
            formatdict = ResolvingDict()
            
            # bring in the command line args for str.format substitution
            formatdict.update(vars(args))
            
            # populate list of variables from command line
            formatdict['varstring'] = varstring
            
            # populate values specific to this input file
            formatdict['inputpath'] = inputpath # the path to the file
            formatdict['inputdirname'] = os.path.dirname(inputpath) # the directory holding the file
            formatdict['inputbasename'] = os.path.splitext(os.path.basename(inputpath))[0] # unix 'basename' without extension not python basename
            
            self.process(formatdict)
        
    
    def process(self, formatdict):
        #print( formatdict['shellcmd'] )
        subprocess.call(formatdict['shellcmd'],shell=True)

if __name__ == "__main__":
    runner = Runner()
    runner.run()