#!/bin/bash
EXCLUDE=(
--exclude="*.md" 
--exclude="*.scss" 
--exclude="sass" 
--exclude=".sass-cache"
)
find ../../../shrimpingit.github.io/ -mindepth 1 -maxdepth 1 -not -name 'CNAME' -and -not -name '.git' -and -not -name '.gitignore' | tail -n +1 | xargs -n1 rm -rf
rsync --verbose --recursive "${EXCLUDE[@]}"  ../../src/content/ ../../../shrimpingit.github.io/ 
./writeraw.py
./writestyled.py --outputdirectory='../../../shrimpingit.github.io/' --serverroot='http://start.shrimping.it/'
