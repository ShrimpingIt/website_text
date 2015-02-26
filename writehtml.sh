#!/bin/bash
PANDOC="echo {}; pandoc"
find . -name '*.md' | sed 's/\(.*\).md$/\1/' | xargs -n1 -I{} bash -c "$PANDOC --include-in-header=header.frag --self-contained {}.md -output {}.html"
find . -name '*.md' | sed 's/\(.*\).md$/\1/' | xargs -n1 -I{} bash -c "cd \`dirname {}\`; $PANDOC --self-contained \`basename {}\`.md -o \`basename {}\`.pdf"
