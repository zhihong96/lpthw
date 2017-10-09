#!usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

# open to_file write,open from_file write in to_file
open(to_file,'w').write(open(from_file).read())
