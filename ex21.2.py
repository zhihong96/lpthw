#!usr/bin/python2.7
# -*- coding: utf-8 -*-

# Extra Credit:
# 1: If you aren't really sure what return does, try writing a few of your own functions and have them return some values. 
# You can return anything that you can put to the right of an =


# EC 1a.
print "\n"
print "\n Now some Extra Credit!\n"
def rt(a, b): #rt = returntest
    print "%d \n+%d" % (a, b)
    print "______"
    return a + b

add = rt(30, 4)

print add
print "\n"

# EC 1b.
def rt2(a, b, c, d):
    print "%d + %d * %d - %d" % (a, b, c, d)
    return a + b * c - d

num = rt2(30, 58, 95, 10) 
print "=", num, "\n"

#EC 1c.
def hello(a, b, c, d):
    return a + b + c + d

w1 = 'Hey '
w2 = 'There '
w3 = 'Buddy '
w4 = 'yeah.'

world = hello(w1, w2, w3, w4)

print world, "\n"

# EC 1d.
s = ' ' #space
def words(a, b, c, d):
    return a + s + b + s + c + s + d
    #return d + s + a + s + b + s + c # Changing it up

print "Pick four words:"
print "Word 1:"
w1 = raw_input('> ')
print "Word 2:"
w2 = raw_input('> ')
print "Word 3:"
w3 = raw_input('> ')
print "Word 4:"
w4 = raw_input('> ')

final = words(w1, w2, w3, w4)
print "\n", final, "\n"

# 2: What you should do is try to figure out the normal formula that would recreate this same set of operations.
# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# Here is a puzzle.
# DIVIDING 50 / 2
# MULTIPLYING 180 * 25
# SUBTRACTING 74 - 4500
# ADDING 35 + -4426
# That becomes:  -4391 Can you do it by hand?


def DIV(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b

def MUL(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def SUB(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def ADD(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

ec2a = DIV(50, 2)
ec2b = MUL(180, ec2a)
ec2c = SUB(74, ec2b)
ec2d = ADD(35, ec2c)

print "That becomes %d Can you do it by hand?" % (ec2d)
print "\n"

# 3: Once you have the formula worked out for the puzzle, get in there and see what happens when you modify the parts of the functions. 
# Try to change it on purpose to make another value.

def DIV(a, b):
    print "%d / %d" % (a, b)
    return a / b

def MUL(a, b):
    print "%d * %d + %d * %d * %d" % (a, b, a, b, a)
    return a * b + a * b * a
    
def SUB(a, b):
    print "%d - %d" % (b, a)
    return b - a

def ADD(a, b):
    print "%d + %d" % (b, b)
    return b + b

ec2a = DIV(50, 2)
ec2b = MUL(180, ec2a)
ec2c = SUB(74, ec2b)
ec2d = ADD(35, ec2c)

print "\n", "Div: %d \nMul: %d \nSub: %d \nAdd: %d" % (ec2a, ec2b, ec2c, ec2d)

print "\n", "That becomes %d Can you do it by hand?" % (ec2d)

# 4: Finally, do the inverse. Write out a simple formula and use the functions in the same way to calculate it.

ecfour = DIV(ec2a, MUL(ec2b, SUB(ec2c, ADD(ec2d, 2))))

print ecfour # I think that is what Zed wanted...
