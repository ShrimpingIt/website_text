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
            outputfiletemplate='../styled/{inputdirname}{sep}{inputbasename}.html',
            shellcmd='echo {inputpath};'+
                    'mkdir -p $(dirname {outputfiletemplate});'+
                    'cat {inputpath}'+
                    '|sed 1d '+
                    '|xqilla -i /dev/stdin {xquery} -v serverroot {serverroot} {varstring} '+
                    '> {outputfiletemplate}'
        )
        parser.add_argument('--xquery',
            default='..{sep}..{sep}src{sep}xquery{sep}index.xq',
            help='A str.format defining the path to an XQuery filter'
        )

    def processinput(self, inputdict):
        #print( inputdict['shellcmd'] )
        subprocess.call(inputdict['shellcmd'],shell=True)


if __name__ == "__main__":
    styler = XqueryStyler()
    styler.run()