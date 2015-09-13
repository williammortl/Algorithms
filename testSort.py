# Sorting Test Program
# Implemented by William M Mortl
# Coded for Python 2.7.9

# imports
from datetime import datetime
from mergeSort import mergeSort
from random import randint
from selectionSort import selectionSort
import sys

# build random list
n = input("\r\nHow long of a list? ")
l = []
for i in range(0, n):
	l.append(randint(0, 10 * n))

# timestamp around sorts
print("\r\nMerge Sort...")
print(datetime.now().time())
ms = mergeSort(l)
print(datetime.now().time())
print("\r\nSelection Sort...")
print(datetime.now().time())
ss = selectionSort(l)
print(datetime.now().time())
print(("\r\nSorted lists the same? %s\r\n") % str(ms == ss))
