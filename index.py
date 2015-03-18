#!/usr/bin/python

import sys,os,copy,threading,traceback,argparse,glob,pdb

from string import Formatter
from watchdog.observers import Observer

# 
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

def main():
    
    parser = argparse.ArgumentParser(
        description='Search recursively from a root for input files'+
                        'matching a specific pattern, run a command'+
                        'on that file. Allows for rich substitution'+
                        'syntax based on python\'s str.format, '+
                        'by both console args and contextual args '+
                        'derived from the matched input files'
    )
    
    parser.add_argument('--rootdir',
        default='.', # default is the current directory
        help='The root directory from which to recursively search files'
    )
    parser.add_argument('--outputfileformat', default='{dirname}' + os.sep + '{basename}.html',
        help='The pattern to use to generate the output file'+
                '{vars} value for the {shellcmd} substitution'
    )
    parser.add_argument('--inputfilematch',
        default='*.md',
        help='The file path pattern (glob) to search each descendant of '+
                '{rootdir} for files to filter'
    )
    parser.add_argument('--xquery',
        default='{rootdir}' + os.sep + 'index.xq',
        help='A str.format defining the path to an XQuery filter'
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
        default='pandoc --from=markdown_github --to=html --standalone {inputpath} '+
                '|sed 1d '+
                '|xqilla -i /dev/stdin {xquery} {varstring} '+
                '> {inputdirname}'+os.sep+'{inputbasename}.html',
        help='A str.format for the shell command to run when an input'+
                'file change is detected, or when updated output is '+
                'forced'
    )

    args = parser.parse_args()
    
    inputpaths = []
    for parent, childdirs, childfiles in os.walk(args.rootdir):
        for childdir in childdirs:
           grandchildmatch = parent + os.sep + childdir + os.sep + args.inputfilematch
           inputpaths += glob.glob(grandchildmatch)

    # populate variables passed in to command line        
    varstring = ''
    if args.var != None:
        for item in args.var:
            varformatdict = dict()
            varformatdict['name'],varformatdict['value']= item
            varstring += str.format(args.varpattern, **varformatdict)    
    
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
                
        print formatdict['shellcmd']
        

if __name__ == "__main__":
    main()