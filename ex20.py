#!usr/bin/python2
# -*- coding: utf-8 -*-

# import argv variables from the sys modlue
from sys import argv

# Assign arguments to variables
script, input_file = argv

# Define a function called print_call to print the whole contents of
# file,with one file object as formal parameter
def print_all(f):
    print f.read()

# Define a function called rewind to make the file reader go back to
# the first byte of the file, with one file object as formal parameter
def rewind(f):
    f.seek(0)

# Define a function called print_a_line to print a line of the file,
# with a integer counter and a file object as formal parameters.
def print_a_line(line_count, f):
    print line_count, f.readline()

# Open a file
current_file = open(input_file)

print "First let's print the whole file:\n"

# Call the print_all function to print the whole file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# Call the rewind function to go back to the beginning of the file
rewind(current_file)

print "Let's print three lines:"

# Set curent line to 1
current_line = 1
print "current_line is equal to: %d\n" % current_line
# Print current line by calling print_a_line function
print_a_line(current_line, current_file)

# Set current line to 2 by adding 1
current_line += 1
print "current_line is equal to: %d\n" % current_line
# Print current line by calling print_a_line function
print_a_line(current_line, current_file)

# Set current line to 3 by adding 1
current_line += 1
print "current_line is equal to: %d\n" % current_line
# Print current line by calling print_a_line function
print_a_line(current_line, current_file)
