# -*- coding: utf-8 -*-

from sys import argv

script, name, age, like = argv

height = raw_input("What's your height?")
weight = raw_input("what's your weight?")

print "My name age like is %s %s %s and my height is %s, weight is %s." % (
    name, age, like, height, weight)
