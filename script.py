# -*- coding: utf-8 -*-

"""
Little script that replaces comment characters to html,
found in the *.hbs files.
"""

import os
import glob

if __name__ == '__main__':

    os.chdir(os.path.join(os.environ['HOME'],
                          "Downloads", "Casper-master"))
    for filename in glob.glob("*.hbs"):
        print(filename)

        # Read in the file
        with open(filename, 'r') as infile :
          filedata = infile.read()

        # Replace the target string
        # Replacing comments
        filedata = filedata.replace('{{!--', '<!--')
        filedata = filedata.replace('--}}', '-->')

        # Write the file out again
        with open(filename, 'w') as outfile:
          outfile.write(filedata)

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

for tag in total_tags:
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tagpage\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()
print("Tags generated, count", total_tags.__len__())
