#!/bin/bash
TLDIR=/home/cefn/Documents/shrimping/git/
#TOHTML="echo {}; pandoc"
#TOHTML="echo {}; multimarkdown --full "
#TOSTYLEDHTML="pandoc --from=markdown_github --to=html --standalone build.md | sed 1d | xqilla -i /dev/stdin ../../editor/xq/index.xq -v serverroot '../../kits/' > build.html"
TOHTML="pandoc --from=markdown_github --to=html --standalone"
TOSTYLED=" saxonb-xquery -s - ${TLDIR}editor/xq/index.xq serverroot=${TLDIR}kits"
find . -name '*.md' | sed 's/\(.*\).md$/\1/' | xargs -n1 -I{} bash -c "$TOHTML {}.md | $TOSTYLED > {}.html"
