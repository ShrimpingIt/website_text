#!/bin/bash
export LANG=en_US.UTF-8
EXCLUDE=(
--exclude="*.md" 
--exclude="*.scss" 
--exclude="sass" 
--exclude=".sass-cache"
)
sass ../../src/content/style/sass/index.scss:../../src/content/style/index.css
find ../../build/raw/ -mindepth 1 -maxdepth 1 -not -name '.gitignore' | tail -n+1 | xargs -n1 rm -rf
find ../../../shrimpingit.github.io/ -mindepth 1 -maxdepth 1 -not -name 'CNAME' -and -not -name '.git' -and -not -name '.gitignore' | tail -n +1 | xargs -n1 rm -rf
rsync --verbose --recursive "${EXCLUDE[@]}"  ../../src/content/ ../../../shrimpingit.github.io/ 
./writeraw.py
./writestyled.py --outputdirectory='../../../shrimpingit.github.io/' --serverroot='http://start.shrimping.it/'
