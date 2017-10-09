# -*- coding: utf-8 -*-

i = raw_input("who is you?")
print "I: %s" % i

print "Do you like her?"
answer1 = raw_input("(is/not)")
print "What do you like about her?"
answer2 = raw_input("(temperament/appearance)")
print "You do not like her anything?"
answer3 = raw_input("(positive/behavior)")
print "I %r like her,i like her %r, i do not like her %r" % (answer1, answer2, answer3)
