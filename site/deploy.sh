#!/bin/bash

python freezer.py

echo "Connecting to server..."
scp -r build lifc1350@cubic.wlu.ca:/wwwhome/rmelnik/public_html/ammcs2015
#rsync -a --ignore-existing build/ lifc1350@cubic.wlu.ca:/wwwhome/rmelnik/public_html/ammcs2015/
