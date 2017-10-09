#!usr/bin/python
# -*- coding: utf-8 -*-

#the sum function
def displaySum(a,b):
  sum = a + b
  print "The sum is: %d" % sum

print "#1:"
displaySum(5,10)                #1


print "#2:"
x=3
k=7                             #2
displaySum(x,k)

print "#3:"
displaySum(5+5, 10+10)          #3

print "#4:"
displaySum(x+5,k+10)            #4

print "#5:"
var1 = int(raw_input("p1: "))   #5
var2 = int(raw_input("p2: "))
displaySum(var1,var2)


def passValue():                #6
  x1 = 100 
  x2 = 200
  displaySum(x1,x2)

print "#6:" 
passValue()
