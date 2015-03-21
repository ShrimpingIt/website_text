#!/usr/bin/python

from shrimpshell import Runner

class PandocRunner(Runner):
    def __init__(self):
        super(PandocRunner,self).__init__()
        self.parser.set_defaults(something='else')

if __name__ == "__main__":
    runner = PandocRunner()
    runner.run()