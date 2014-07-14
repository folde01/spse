#!/usr/bin/env python

import sys
import os

def recurse(dir, level):
  lsdir = os.listdir(dir)  
  for i in lsdir:
    absI = os.path.join(dir, i)
    print '-'*4*level + i 
    if os.path.isdir(absI):
      recurse(os.path.join(absI), level+1)

recurse(sys.argv[1], 0)
