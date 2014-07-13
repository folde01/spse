#!/usr/bin/env python

class NotOneCharError(Exception):
  def __init__(self, val):
    self.val = val
  def __str__(self):
    return repr(self.val)

s = raw_input("enter a character: ")

print 'u entered %s' % s 

if not len(s) == 1:
  raise NotOneCharError("That wasn't one char!")
