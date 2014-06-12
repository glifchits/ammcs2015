#!/bin/bash

python freezer.py
cp static/files/google82f44dcd8eab57e0.html build && echo "copied google validation html"
echo "Connecting to server..."
#scp -r build/ lifc1350@cubic.wlu.ca:/wwwhome/rmelnik/public_html/ammcs2015
rsync -avz --progress build/ lifc1350@cubic.wlu.ca:/wwwhome/rmelnik/public_html/ammcs2015/
