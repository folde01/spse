#!/usr/bin/env python

import Calc
from Calc import SciCalc 

print '10 + 20 = %d' % Calc.quickAdd(10,20)

x = Calc.Calc(40,41)
print '40 + 41 = %d' % x.add()

y = SciCalc(2,3)
print '2 pow 3 = %d' % y.pow()


