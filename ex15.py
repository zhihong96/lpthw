#!usr/bin/python
# -*- coding: utf-8 -*-

# import argv variables from sys module
from sys import argv

# get argv variables
script, filename = argv

# open file
txt = open(filename)

# print a string with the filename
print "Here's your file %r:" % filename
# print all contents of the  file 
print txt.read()

# close the file
txt.close()

# prompt to type the file name again
print "Type the filename again:"
# input the new file name
file_again = raw_input(">")

# open the new selected file
txt_again = open(file_again)

# print the contents of the new selscted file
print txt_again.read()

# close the file
txt_again.close()
