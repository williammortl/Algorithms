# Heap Building Algorithms
# Implemented by William M Mortl

# imports
import sys
from random import randint
import mergeSort

# get the parent of the node at i
def parent(list, i):
	if (i == 0):
		return 0
	else:
		return (i - 1) / 2

# left child of the node at i
def left(list, i):
	return (2 * i) + 1

# right child of the node at i
def right(list, i):
	return (2 * i) + 2

# heapify with a comparator, can build max or min heaps
def heapify(list, i, comparator, s):
	l = left(list, i)
	r = right(list, i)
	if ((l < s) and (comparator(list[l], list[i]))):
		maxmin = l
	else:
		maxmin = i
	if ((r < s) and (comparator(list[r], list[maxmin]))):
		maxmin = r
	if (maxmin != i):
		tmp = list[i]
		list[i] = list[maxmin]
		list[maxmin] = tmp
		heapify(list, maxmin, comparator, s)
	return list

# converts a list to a heap
def buildHeap(list, comparator):
	s = len(list)
	midpoint = (len(list) / 2) - 1
	for i in xrange(midpoint, -1, -1):
		heapify(list, i, comparator, s)
	return list

# a maximum heap comparator
def maxComparator(l, r):
	return (l > r)

# a minimum heap comparator
def minComparator(l, r):
	return (l < r)

# print heap
def printHeap(list):
	s = len(list)
	current = 0
	l = left(list, current)
	r = right(list, current)
	print("Printing the entire heap:")
	print("------------------------------------------------------------")
	while ((l < s) and (r < s)):
		print(("  Parent:\t[%s] %s") % (str(current), str(list[current])))
		print(("Children:\t[%s] %s - [%s] %s") % (str(l), str(list[l]), str(r), str(list[r])))
		print("------------------------------------------------------------")
		current = current + 1
		l = left(list, current)
		r = right(list, current)

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print("\r\nHeap Algorithms by William M Mortl")
		print("Usage: python heap.py {+ for max | - for min} \"{comma seperated list of values to make into a heap}\"")
		print("Example: python heap.py + \"9,111,2,31,1,0\"\r\n")
	else:
		maxOrMin = "Min" if sys.argv[1].strip() == "-" else "Max"
		listToHeap = map(int, sys.argv[2].split(","))
		print(("\r\nBuilding a heap from:\r\n%s") % str(listToHeap))
		heapList = buildHeap(listToHeap, minComparator if (maxOrMin == "Min") else maxComparator)
		print(("%s heap:\r\n%s") % (maxOrMin, str(heapList)))
		printHeap(heapList)
		print("")