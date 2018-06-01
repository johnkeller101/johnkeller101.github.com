#!/bin/bash

# go to the correct directory
cd "/Users/john/Sync/Important Documents/johnkeller101.github.io"

echo "Running python script to generate tags and authors"

python script.py

echo "Updating the github repo for https://john.coffee"

# generate timestamp variable
current_time=$(date "+%Y.%m.%d-%H.%M.%S")

git add .
git commit -m "$current_time"
git push -u origin master