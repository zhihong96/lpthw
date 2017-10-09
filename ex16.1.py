#!usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

# target and ex16 can change.
print "opening file %s." % filename
target = open(filename)
ex16 = target.read()
print ex16
target.close()
