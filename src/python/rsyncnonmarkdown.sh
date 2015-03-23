#!/bin/bash
rsync --recursive --exclude '*.md' ../../src/markdown/ ../../build/raw/
rsync --recursive --exclude '*.md' ../../src/markdown/ ../../build/styled/
