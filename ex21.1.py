#!usr/bin/python2.7
# -*- coding: utf-8 -*-

def a(x, y):
    print "A %d + %d" % (x, y)
    return x + y

def b(x, y):
    print "B %d - %d" % (x, y)
    return x - y

def c(x, y):
    print "C %d * %d" % (x, y)
    return x * y

def d(x, y):
    print "D %d / %d" % (x, y)
    return x / y

print "Let's do some math with just function!"

age = a(30, 5)
height = b(78, 4)
weight = c(90, 2 )
iq = d(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# count 10 * 180 + (50 / 2)
what = c(10, d(iq, 2))

print "That becones:", what
