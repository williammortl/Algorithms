# Selection Sort Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(n ^ 2)
# python selectionSort.py "9,111,2,31,7,0,5,4,3,1,100001,32,31,27,16,15,999,3,3,3,3,100000000,7"

# imports
import copy
from mergeSort import mergeSort
import sys

# in place selection sort
def selectionSort(listToSort):
	for i in range(0, len(listToSort)):
		minIndex = i
		for j in range(i, len(listToSort)):
			if (listToSort[j] <= listToSort[minIndex]):
				minIndex = j
		tmp = listToSort[i]
		listToSort[i] = listToSort[minIndex]
		listToSort[minIndex] = tmp
	return listToSort

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nSelection Sort by William M Mortl")
		print("Usage: python selectionSort.py \"{comma seperated list of values to sort}\"")
		print("Example: python selectionSort.py \"9,111,2,31,1,0\"\r\n")
	else:
		listToSort = map(int, sys.argv[1].split(","))
		print(("\r\nSorting:\r\n%s") % str(listToSort))
		mergeSorted = mergeSort(copy.deepcopy(listToSort))
		selectionSorted = selectionSort(copy.deepcopy(listToSort))
		print(("Merge Sorted list:\r\n%s") % str(mergeSorted))
		print(("Selection Sorted list:\r\n%s") % str(selectionSorted))
		print(("Lists equal? %s\r\n") % str(mergeSorted == selectionSorted))
