#!/usr/bin/python

import subprocess

from shrimpshell import Runner

class MarkdownExporter(Runner):
    def __init__(self):
        super(MarkdownExporter,self).__init__()
        
    def initparser(self, parser):
        super(MarkdownExporter,self).initparser(parser)
        parser.set_defaults(
            workingdirectory='../content',
            outputdirectory='../../build/raw',
            shellcmd='echo {inputpath};'+ # the .md source file path
                    'mkdir -p $(dirname {outputfiletemplate});'+ # lazy-create containing directory
                    'pandoc --from=markdown_github --to=html --standalone {inputpath}'+ # export via pandoc to stdout
                    '|sed 1d' # removes XML declaration before writing
                    '> {outputfiletemplate}' # write out to the .html file
        )

    def runcommand(self, inputdict):
        #print( inputdict['shellcmd'] )
        subprocess.call(inputdict['shellcmd'],shell=True)


if __name__ == "__main__":
    exporter = MarkdownExporter()
    exporter.execute()
