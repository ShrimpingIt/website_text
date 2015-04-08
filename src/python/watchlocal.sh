#!/bin/bash
./rsyncnonmarkdown.sh
sass ../../src/content/style/sass/index.scss:../../src/content/style/index.css --watch &
sass ../../src/content/style/sass/index.scss:../../build/styled/style/index.css --watch &
./writeraw.py
./writestyled.py
./writeraw.py --norun --watch &
./writestyled.py --norun --watch &

