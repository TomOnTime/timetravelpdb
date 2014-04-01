#!/usr/bin/python2.6

import timetravelpdb

x = 500

def add10(number):
  return number + 10

print "foo"
print "bar"
print "baz"

timetravelpdb.set_trace()

y = add10(x)
x = 15
z = x + y

for i in range(15):
  print "THE NUMBER IS", i
  y = add10(i)
