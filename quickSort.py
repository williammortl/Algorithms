# Quick Sort Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(n ^ 2), however, this on average is the fastest sorting algorithm
# python quickSort.py "9,111,2,31,7,0,5,4,3,1,100001,32,31,27,16,15,999,3,3,3,3,100000000,7"

# imports
import copy
from mergeSort import mergeSort
import random
import sys

# in place quick sort function, quick sort range [i, j] <- inclusive
def quickSort(listToSort, i, j):
	k = j - i
	if (k == 1):
		if (listToSort[i] > listToSort[j]):
			tmp = listToSort[i]
			listToSort[i] = listToSort[j]
			listToSort[j] = tmp
	elif (k > 1):
		p = random.randint(i, j)
		tmp = listToSort[i]
		listToSort[i] = listToSort[p]
		listToSort[p] = tmp
		i0 = i
		p = i
		start = p + 1
		for i in range(start, (j + 1)):
			if (listToSort[i] <= listToSort[p]):
				tmp = listToSort[i]
				listToSort[(p + 1) : (i + 1)] = listToSort[p : i]
				listToSort[p] = tmp
				p = p + 1
		quickSort(listToSort, i0, p - 1)
		quickSort(listToSort, p + 1, j)
	return listToSort

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nQuick Sort by William M Mortl")
		print("Usage: python quickSort.py \"{comma seperated list of values to sort}\"")
		print("Example: python quickSort.py \"9,111,2,31,1,0\"\r\n")
	else:
		listToSort = map(int, sys.argv[1].split(","))
		print(("\r\nSorting:\r\n%s") % str(listToSort))
		mergeSorted = mergeSort(copy.deepcopy(listToSort))
		quickSorted = quickSort(copy.deepcopy(listToSort), 0, len(listToSort) - 1)
		print(("Merge Sorted list:\r\n%s") % str(mergeSorted))
		print(("Quick Sorted list:\r\n%s") % str(quickSorted))
		print(("Lists equal? %s\r\n") % str(mergeSorted == quickSorted))
