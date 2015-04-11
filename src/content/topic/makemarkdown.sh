#!/bin/bash
find . -name '*.html' | xargs -n1 -I{} bash -c "iconv -t utf-8 {} | pandoc -f html -t markdown_github | iconv -f utf-8  > {}.md"
