#!usr/bin/python
# -*- coding: utf-8 -*-

# import argv variables from sys module
from sys import argv

# get argv variables
script, filename = argv

# print string with the filename
print "We're going to erase %r." % filename
print "If you don't want that,hit CTRL-C(^C)."
print "If you do want that, hit RETURN."

# input string
raw_input("?")

# open file
print "Opening the file..."
target = open(filename,'w')

# emptles file
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

# input three lines string
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# write to file
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# close file
print "And finally, we close it."
target.close()
