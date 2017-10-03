# -*- coding: utf-8 -*-

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too 
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists. first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # apped is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i


""" Python List Methods
    append() - Add an element to the end of the list
    extend() - Add all elements of a list to the another list
    insert() - Insert an item at the defined index
    remove() - Removes an item from the list
    pop() - Removes and returns an element at the given index
    clear() - Removes all items from the list
    index() - Returns the index of the first matched item
    count() - Returns the count of number of items passed as an argument
    sort() - Sort items in a list in ascending order
    reverse() - Reverse the order of items in the list
    copy() - Returns a shallow copy of the list
"""

