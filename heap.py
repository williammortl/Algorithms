# Heap Building Algorithms
# Implemented by William M Mortl
# Coded for Python 2.7.9
# To build heap: O(n)
# python heap.py + "9,111,2,31,7,0,5,4,3,1,100001,32,31,27,16,15,999,3,3,3,3,100000000,7"

# imports
import sys

# get the parent of the node at i
def parent(list, i):
	if (i <= 0):
		return -1
	else:
		return (i - 1) / 2

# left child of the node at i
def left(list, i):
	s = len(list)
	leftChild = (2 * i) + 1
	return leftChild if (leftChild < s) else -1

# right child of the node at i
def right(list, i):
	s = len(list)
	rightChild = (2 * i) + 2
	return rightChild if (rightChild < s) else -1

# is this node left child? if not we know we're the root or a right node	
def isLeftNode(list, i):
	return true if (left(list, parent(list, i)) == i) else false

# a maximum heap comparator
def maxComparator(l, r):
	return (l > r)

# a minimum heap comparator
def minComparator(l, r):
	return (l < r)

# get sibling
def sibling(list, i):
	s = len(list)
	sib = -1
	if (i > 0):
		if (isLeftNode(list, i) == true):
			sib = right(list, parent(list, i))
		else:
			sib = left(list, parent(list, i))
	return sib if (sib < s) else -1

# heapify with a comparator, can build max or min heaps
def heapify(list, i, comparator, s):
	l = left(list, i)
	r = right(list, i)
	if ((l < s) and (l >= 0) and (comparator(list[l], list[i]))):
		maxmin = l
	else:
		maxmin = i
	if ((r < s) and (r >= 0) and (comparator(list[r], list[maxmin]))):
		maxmin = r
	if (maxmin != i):
		tmp = list[i]
		list[i] = list[maxmin]
		list[maxmin] = tmp
		heapify(list, maxmin, comparator, s)
	return list

# converts a list to a heap
def buildHeap(listToHeap, comparator):
	s = len(listToHeap)
	midpoint = (s / 2) - 1
	for i in xrange(midpoint, -1, -1):
		listToHeap = heapify(listToHeap, i, comparator, s)
	return listToHeap

# insert into heap
def insert(list, number, comparator):
	list.append(number)
	c = len(list) - 1
	p = parent(list, c)
	while (p >= 0):
		 if (comparator(list[c], list[p])):
		 	tmp = list[p]
		 	list[p] = list[c]
		 	list[c] = tmp
		 	c = p
		 	p = parent(list, c)
		 else:
		 	break
	return list

# deletes a node, if this is not the root node, reconvert to a heap
# 	note: removing anything other than the root node, is not usually supported
def delete(list, i, comparator):
	s = len(list)
	newList = []
	if (i == 0):
		if (s > 1):
			tmp = list[s - 1]
			newList = list[1 : (s - 1)]
			newList.insert(0, tmp)
			newList = heapify(newList, 0, comparator, s - 1)
	elif (i == (s - 1)):
		newList = list[0 : i]
	else:
		newList = list[0 : i] + list[(i + 1) : s]
		newList = buildHeap(newList, comparator)
	return newList

# print heap
def printHeap(list):
	s = len(list)
	current = 0
	print("Printing the entire heap:")
	print("-" * 50)
	while (current < s):
		l = left(list, current)
		r = right(list, current)
		lVal = str(list[l]) if ((l >= 0) and (l < len(list))) else "nil"
		rVal = str(list[r]) if ((r >= 0) and (r < len(list))) else "nil"
		if ((l >= 0) or (r >= 0)):
			print(("  Parent:\t[%s] %s") % (str(current), str(list[current])))
			print(("Children:\t[%s] %s - [%s] %s") % (str(l), lVal, str(r), rVal))
			print("-" * 50)
		current = current + 1
		
# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print("\r\nHeap Algorithms by William M Mortl")
		print("Usage: python heap.py {+ for max | - for min} \"{comma seperated list of values to make into a heap}\"")
		print("Example: python heap.py + \"9,111,2,31,1,0\"\r\n")
	else:
		maxOrMin = "Min" if sys.argv[1].strip() == "-" else "Max"
		heapList = map(int, sys.argv[2].split(","))
		print(("\r\nBuilding a heap from:\r\n%s\r\n") % str(heapList))
		comparator = minComparator if (maxOrMin == "Min") else maxComparator
		heapList = buildHeap(heapList, comparator)
		print(("%s heap:\r\n%s\r\n") % (maxOrMin, str(heapList)))
		numberToInsert = 777777777777
		heapList = insert(heapList, numberToInsert, comparator)
		print(("Heap after inserting %s:\r\n%s\r\n") % (str(numberToInsert), str(heapList)))
		numberToInsert = -1
		heapList = insert(heapList, numberToInsert, comparator)
		print(("Heap after inserting %s:\r\n%s\r\n") % (str(numberToInsert), str(heapList)))
		heapList = delete(heapList, 0, comparator)
		print(("Heap after deleting the root:\r\n%s\r\n") % (str(heapList)))
		s = len(heapList)
		heapList = delete(heapList, s / 2, comparator)
		print(("Heap after deleting the midpoint:\r\n%s\r\n") % (str(heapList)))
		s = len(heapList)
		heapList = delete(heapList, s - 1, comparator)
		print(("Heap after deleting the last element:\r\n%s\r\n") % (str(heapList)))
		printHeap(heapList)
		print("")