#!/usr/bin/python

import subprocess

from shrimpshell import Runner

class MarkdownExporter(Runner):
    def __init__(self):
        super(MarkdownExporter,self).__init__()
        
    def initparser(self, parser):
        super(MarkdownExporter,self).initparser(parser)
        parser.set_defaults(
            workingdirectory='../markdown',
            outputdirectory='../../build/raw',
            shellcmd='echo {inputpath};'+
                    'mkdir -p $(dirname {outputfiletemplate});'+
                    'pandoc --from=markdown_github --to=html --standalone {inputpath}'+
                    '> {outputfiletemplate}'
        )

    def runcommand(self, inputdict):
        #print( inputdict['shellcmd'] )
        subprocess.call(inputdict['shellcmd'],shell=True)


if __name__ == "__main__":
    exporter = MarkdownExporter()
    exporter.execute()