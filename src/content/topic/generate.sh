#!/bin/bash
find /home/cefn/Documents/code/bbc/iot/my_repositories/radiotagfob-jasmine-merge/ConceptNetwork/src/technology/ -name '*.html' | xargs -n1 -I[] bash -c 'xpath [] "//div[@id=\"content\"]/*" > $(basename "[]")'
