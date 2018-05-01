import numpy as np
from pylab import *

a = np.array([1,2,3])
b = np.array([2,4,6])
print a**2 * b

M = 9
xlist = np.linspace(0, 2.5, 10)
print "xlist:",xlist
for i in range(M + 1):
    for j in range(M + 1):
        print "i:",i,"  j:",j,"   ",xlist ** (i + j)
        print (xlist ** (i + j)).sum()
        temp = (xlist ** (i + j)).sum()



#
# N = 10
# xList = np.linspace(0,1,N)
# print xList
#
# diff = np.random.normal(0,0.2,xList.size)
#
# yList = np.sin(2*np.pi*xList) + diff
#
# print yList
