#!/usr/bin/python
                                                                           
import subprocess

from shrimpshell import Runner

class XqueryStyler(Runner):
    def __init__(self):
        super(XqueryStyler,self).__init__()
        
    def initparser(self, parser):
        super(XqueryStyler,self).initparser(parser)
        parser.set_defaults(
            inputfileglob='*.html',
            workingdirectory='../../build/raw/',
            outputdirectory='../styled',
            shellcmd='echo {inputpath};'+
                    'mkdir -p $(dirname {outputfiletemplate});'+
                    'cat {inputpath}'+
                    '|sed 1d '+
                    "|xqilla -i /dev/stdin {xquery} -v sourcepath {inputpath} -v serverroot '{serverroot}' -v allsourcepaths '{inputpaths}' {varstring} "+
                    '|xmlindent '+
                    '| sed -e \'1i<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\\\' '
                    '> {outputfiletemplate}',
            # to get nicely indented XHTML
            # consider adding perltidy -i=2 -ce
            burstwindow=0.25,
            watchextra=["../../src/xquery"]
        )
        parser.add_argument('--xquery',
            default='..{sep}..{sep}src{sep}xquery{sep}index.xq',
            help='A str.format defining the path to an XQuery filter'
        )
        parser.add_argument('--serverroot',
            default='/home/cefn/Documents/shrimping/git/website_text/build/styled/',
            help='Used to populate root-relative urls (e.g. for css references)'
        )

    def runcommand(self, inputdict):        
        #print( inputdict['shellcmd'] )
        subprocess.call(inputdict['shellcmd'],shell=True)


if __name__ == "__main__":
    styler = XqueryStyler()
    styler.execute()
