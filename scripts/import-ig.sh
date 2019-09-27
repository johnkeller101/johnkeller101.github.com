#!/bin/bash

echo "INSTAGRAM TO JEKYLL IMPORTER"

echo "[?] Which Instagram post would you like to import?"
read post

echo "[?] What is the title of your new post?"
read title

echo "[?] What should the publish date of the post be? (y-m-d)"
read date

# Set the directories
postDir="/Users/john/Sync/Important Documents/johnkeller101.github.io/_posts"
imgDir="/Users/john/Sync/Important Documents/johnkeller101.github.io/assets/images/instagram"
shortImgDir="/assets/images/instagram"

# Format filename
fileName=$(echo "$date-$title" | iconv -t ascii//TRANSLIT | sed -E s/[^a-zA-Z0-9]+/-/g | sed -E s/^-+\|-+$//g | tr A-Z a-z)
path="$postDir/$fileName.md"

# Show confirmation on screen
echo "Starting import"
echo "--> importing post with id '$post'"
echo "--> output file: $fileName.md"

# Download the images
echo "--> import images"
wget --output-document="$imgDir/$fileName.jpg" "https://www.instagram.com/p/$post/media"
wget --output-document="$imgDir/${fileName}_large.jpg" "https://www.instagram.com/p/$post/media?size=l"
wget --output-document="$imgDir/${fileName}_thumbnail.jpg" "https://www.instagram.com/p/$post/media?size=t"

# Get post data from instagram
postData=$(curl -s "https://api.instagram.com/oembed/?url=http://instagr.am/p/$post" | jq -r '.html')

# Output markdown file
content="---
layout: post
current: post
navigation: True
tags: group-rides cycling
class: post-template
subclass: 'post tag-rides'
author: john

title: '$title'
date: $date
instagram_id: $post
thumb: $shortImgDir/$fileName.jpg
post_image: $shortImgDir/$fileName.jpg
post_image_large: $shortImgDir/${fileName}_large.jpg
post_image_small: $shortImgDir/${fileName}_thumbnail.jpg
---

<!-- begin ig snippet -->"
echo "$content" >> "$path"
echo "$postData" >> "$path"
echo "<!-- end ig snippet -->" >> "$path"

echo "IMPORT COMPLETE"