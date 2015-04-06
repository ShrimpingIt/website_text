#!/bin/bash
find ../../build/raw/ -type f -not -name '.gitignore' -delete
find ../../build/styled/ -type f -not -name '.gitignore' -delete
rsync --verbose --recursive --exclude '*.md' ../../src/content/ ../../build/raw/
rsync --verbose --recursive --exclude '*.md' ../../src/content/ ../../build/styled/
