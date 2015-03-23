#!/usr/bin/python

import subprocess

from shrimpshell import Runner

class XqueryStyler(Runner):
    def __init__(self):
        super(XqueryStyler,self).__init__()
        
    def initparser(self, parser):
        super(XqueryStyler,self).initparser(parser)
        parser.set_defaults(
            serverroot='/home/cefn/Documents/shrimping/git/kits/build/styled/',
            inputfileglob='*.html',
            workingdirectory='../../build/raw/',
            outputdirectory='../styled',
            outputfiletemplate='{outputdirectory}/{inputdirname}/{inputbasename}.html',
            shellcmd='echo {inputpath};'+
                    'mkdir -p $(dirname {outputfiletemplate});'+
                    'cat {inputpath}'+
                    '|sed 1d '+
                    '|xqilla -i /dev/stdin {xquery} -v serverroot {serverroot} -v inputpaths "{inputpaths}" {varstring} '+
                    '> {outputfiletemplate}',
            burstwindow=0.25,
            watch=True,
            watchextra=["../../src/xquery"]
        )
        parser.add_argument('--xquery',
            default='..{sep}..{sep}src{sep}xquery{sep}index.xq',
            help='A str.format defining the path to an XQuery filter'
        )

    def runcommand(self, inputdict):        
        #print( inputdict['shellcmd'] )
        subprocess.call(inputdict['shellcmd'],shell=True)


if __name__ == "__main__":
    styler = XqueryStyler()
    styler.execute()