#!usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename

raw_input("?")

print "OPening the fiel..."
target = open(filename, 'w')

print "Trubcaring the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

lines = [raw_input("Lines %r :" % i) for i in range(1,4)]

for line in lines:
    target.write(line + "\n")

print "And finally, we close it."
target.close()
