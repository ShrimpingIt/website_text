#!/bin/bash
watchmedo shell-command --drop --recursive --command="cd ../../src/python;./writestyled.py"
