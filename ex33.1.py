# -*- coding: utf-8 -*-

i = 0
numbers = []

def theloop(numb, plusnum):
    global i
    while i < plusnum:
	print "At the top of i is %d" % i
	numbers.append(i)

	i = i + numb
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

	print "The numbers: "
	for num in numbers:
	    print num

theloop(2, 7)

