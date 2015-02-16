# Heap Sort Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(n log n)

# imports
import sys
from random import randint
import mergeSort
import heap

# heap sort, use maxComparator for ascending and minComparator for descending
def heapSort(list):
	list = heap.buildHeap(list, heap.maxComparator)
	s = len(list)
	for i in xrange((s - 1), 0, -1):
		tmp = list[0]
		list[0] = list[i]
		list[i] = tmp
		s = s - 1
		heap.heapify(list, 0, heap.maxComparator, s)
	return list

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nHeap Sort by William M Mortl")
		print("Usage: python heapSort.py \"{comma seperated list of values to sort}\"")
		print("Example: python heapSort.py \"9,111,2,31,1,0\"\r\n")
	else:
		listToSort = map(int, sys.argv[1].split(","))
		print(("\r\nSorting:\r\n%s") % str(listToSort))
		mergeSorted = mergeSort.mergeSort(listToSort)
		heapSorted = heapSort(listToSort)
		print(("Merge Sorted list:\r\n%s") % str(mergeSorted))
		print(("Heap Sorted list:\r\n%s") % str(heapSorted))
		print(("Lists equal? %s\r\n") % str(mergeSorted == heapSorted))
