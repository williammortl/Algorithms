# Heap Sort Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(n log n)
# python heapSort.py "9,111,2,31,7,0,5,4,3,1,100001,32,31,27,16,15,999,3,3,3,3,100000000,7"

# imports
import copy
import heap
from mergeSort import mergeSort
import sys

# heap sort, use maxComparator for ascending and minComparator for descending
def heapSort(listToSort):
	listToSort = heap.buildHeap(listToSort, heap.maxComparator)
	s = len(listToSort)
	listLength = s
	for i in xrange((listLength - 1), 0, -1):
		tmp = listToSort[0]
		listToSort[0] = listToSort[i]
		listToSort[i] = tmp
		s = s - 1
		heap.heapify(listToSort, 0, heap.maxComparator, s)
	return listToSort

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nHeap Sort by William M Mortl")
		print("Usage: python heapSort.py \"{comma seperated list of values to sort}\"")
		print("Example: python heapSort.py \"9,111,2,31,1,0\"\r\n")
	else:
		listToSort = map(int, sys.argv[1].split(","))
		print(("\r\nSorting:\r\n%s") % str(listToSort))
		mergeSorted = mergeSort(copy.deepcopy(listToSort))
		heapSorted = heapSort(copy.deepcopy(listToSort))
		print(("Merge Sorted list:\r\n%s") % str(mergeSorted))
		print(("Heap Sorted list:\r\n%s") % str(heapSorted))
		print(("Lists equal? %s\r\n") % str(mergeSorted == heapSorted))
