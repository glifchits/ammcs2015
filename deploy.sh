#!/bin/bash

gulp styles
python freezer.py
cp static/files/google82f44dcd8eab57e0.html build && echo "copied google validation html"
chmod -R 775 build/
echo "Connecting to server..."
#scp -r build/ lifc1350@cubic.wlu.ca:/wwwhome/rmelnik/public_html/ammcs2015
rsync -avz --progress build/ lifc1350@cubic.wlu.ca:/wwwhome/rmelnik/public_html/ammcs2015/
