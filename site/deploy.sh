#!/bin/bash

python freezer.py

files="";
if [ "$1" = "--html" ]; then
  echo "deploying html files only"
  files="build/**/*.html";
else
  files="build/*"
fi

echo "Connecting to server..."
scp -r $files lifc1350@cubic.wlu.ca:/wwwhome/rmelnik/public_html/ammcs2015/
