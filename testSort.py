# Sorting Test Program
# Implemented by William M Mortl
# Coded for Python 2.7.9

# imports
import sys
import random
import datetime
import selectionSort

# build random list
n = input("How long of a list? ")
l = []
for i in range(0, n):
	l.append(random.randint(0, 10 * n))

# timestamp around sort
print(datetime.datetime.now().time())
v = selectionSort.selectionSort(l)
print(datetime.datetime.now().time())
