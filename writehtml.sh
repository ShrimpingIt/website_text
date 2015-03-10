#!/bin/bash
#TOHTML="echo {}; pandoc"
TOHTML="echo {}; multimarkdown -f "
find . -name '*.md' | sed 's/\(.*\).md$/\1/' | xargs -n1 -I{} bash -c "$TOHTML {}.md > {}.html"
