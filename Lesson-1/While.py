#!/usr/bin/python

age = 20

while age > 10:
  age = int(raw_input("age please: "))
  if age > 10:
    print "age > 10"
  else:
    print "age <= 10"
else:
  print "done"

