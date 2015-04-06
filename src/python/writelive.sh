#!/bin/bash
rsync --verbose --recursive --exclude '*.md' ../../src/content/ ../../../shrimpingit.github.io/ 
/
./writeraw.py
./writestyled.py --outputdirectory="../../../shrimpingit.github.io/" --serverroot '/'
