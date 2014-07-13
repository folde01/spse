#!/usr/bin/env python

class Calc:
  
  gg = 99

  def __init__(self, ina, inb):
    self.a = ina
    self.b = inb

  
  def add(self):
    return self.a + self.b

  def mul(self):
    return self.a * self.b
    
class SciCalc(Calc):


  def add(self):
    return 1111

  def pow(self):
    global f
    f = 40
    return pow(self.a, self.b)
 
newCalc = Calc(10,20)
print 'a + b = %d' % newCalc.add()
print 'a * b = %d' % newCalc.mul()
newCalc.gg = 1000
print newCalc.gg
newCalc2 = Calc(10,20)
print newCalc2.gg
Calc.gg = 1001
print newCalc2.gg
    
newSciCalc = SciCalc(10,20)
print 'a pow b = %d' % newSciCalc.pow()
print 'a + b = %d' % newSciCalc.add()
print f
print newSciCalc.gg

def quickAdd(a, b):
  return a + b
