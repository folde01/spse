#!/usr/bin/env python

import sys

str = sys.argv[1]
file = sys.argv[2]

def srchFile(str, file):
  fo = open(file, "r")
  for line in fo.readlines():
    if srch(line, str):
      print line.strip()
  fo.close()
  
def srch(si, sf):
  matched = False
  i = 0
  while matched == False and i < len(si):
    if srchFrom(si, sf, i):
      matched = True 
    i += 1
  return matched

def srchFrom(si, sf, siInd):
  matched = True
  i = siInd
  j = 0 
  while matched == True and j < len(sf):
    if si[i:i+1] != sf[j:j+1]:
      matched = False
    i += 1
    j += 1  
  return matched
  
srchFile(str, file)

#print srchFrom("abcUSBdef", "abcUSBde", 0)
#print srchFrom("abcUSBdef", "USBde", 4)
#print srch("abcUSBdef", "abcUSBd")
#srchFile("usb.txt", "usb")
