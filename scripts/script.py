# -*- coding: utf-8 -*-

import os
import glob


#!/usr/bin/env python

'''
tag_generator.py

Copyright 2017 Long Qian
Contact: lqian8@jhu.edu

This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
'''

post_dir = '_posts/'
tag_dir = 'tag/'

filenames = glob.glob(post_dir + '*md')

total_tags = []
for filename in filenames:
    f = open(filename, 'r')
    crawl = False
    for line in f:
        if crawl:
            current_tags = line.strip().split()
            if current_tags[0] == 'tags:':
                total_tags.extend(current_tags[1:])
                crawl = False
                break
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()
total_tags = set(total_tags)

old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)
    
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

prt_txt = ""

for tag in total_tags:
    tag_desc = ''
    tag_img = ''
    if tag == 'rides':
      tag_desc = 'A collection of my favorite rides'
      tag_img = 'assets/images/rides-bg.jpg'
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    if tag == 'cycling' or tag == 'projects':
        write_str = '---\nlayout: tag-page\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag
    else:
        write_str = '---\nlayout: tag\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag
    if len(tag_desc) > 1:
      write_str = write_str + '\ndescription: ' + tag_desc
    if len(tag_img) > 1:
      write_str = write_str + '\ncover: ' + tag_img
    write_str = write_str + '\n---\n'
    f.write(write_str)
    f.close()
    prt_txt = prt_txt + tag + ", "

print("Generated", total_tags.__len__(), "tags:",prt_txt[:-2])


# attempted custom author pages using no plugins

post_dir = '_posts/'
tag_dir = 'author/'

filenames = glob.glob(post_dir + '*md')

total_tags = []
for filename in filenames:
    f = open(filename, 'r')
    crawl = False
    for line in f:
        if crawl:
            current_tags = line.strip().split()
            if current_tags[0] == 'author:':
                total_tags.extend(current_tags[1:])
                crawl = False
                break
        if line.strip() == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
    f.close()
total_tags = set(total_tags)

old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)
    
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

prt_txt = ""

for tag in total_tags:
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: author\ntitle: \"' + tag + '\"\nauthor: ' + tag
    if len(tag_desc) > 1:
      write_str = write_str + '\ndescription: ' + tag_desc
    if len(tag_img) > 1:
      write_str = write_str + '\ncover: ' + tag_img
    write_str = write_str + '\n---\n'
    f.write(write_str)
    f.close()
    prt_txt = prt_txt + tag + ", "

print("Generated", total_tags.__len__(), "authors:",prt_txt[:-2])







