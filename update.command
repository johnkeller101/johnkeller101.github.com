#!/bin/bash

# go to the correct directory
cd "/Users/john/Sync/Important Documents/johnkeller101.github.io"

echo "Generating tags and authors"
echo "----------------------------------"
python3 scripts/script.py
echo "Generating map files for posts"
echo "----------------------------------"
python3 scripts/generateRideMaps.py
echo "----------------------------------"
echo "Updating the github repo for https://john.coffee"
echo "----------------------------------"
# generate timestamp variable
current_time=$(date "+%Y.%m.%d-%H.%M.%S")

git add .
git reset -- _drafts/
git commit -m "$current_time"
git push -u origin master
echo "----------------------------------"