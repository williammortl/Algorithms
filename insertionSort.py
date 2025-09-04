# Insertion Sort Algorithm
# Implemented by William M Mortl
# O(n ^ 2)
# python insertionSort.py "9,111,2,31,7,0,5,4,3,1,100001,32,31,27,16,15,999,3,3,3,3,100000000,7"

# imports
from copy import deepcopy
from mergeSort import mergeSort
import sys

# in place insertion sort
def insertionSort(listToSort):
	s = len(listToSort)
	itr = 1
	while(itr < s):
		valInsert = listToSort[itr]
		for i in range((itr - 1), -1, -1):
			valCompare = listToSort[i]
			if (valCompare < valInsert):
				listToSort[(i + 2) : (itr + 1)] = listToSort[(i + 1): (itr)]
				listToSort[i + 1] = valInsert;
				break
			elif ((i == 0) and (valCompare > valInsert)):
				listToSort[1 : (itr + 1)] = listToSort[i : itr]
				listToSort[i] = valInsert;
		itr = itr + 1
	return listToSort

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nInsertion Sort by William M Mortl")
		print("Usage: python insertionSort.py \"{comma seperated list of values to sort}\"")
		print("Example: python insertionSort.py \"9,111,2,31,1,0\"\r\n")
	else:
		listToSort = list(map(int, sys.argv[1].split(",")))
		print("\r\nSorting:\r\n{}\r\n".format(listToSort))
		mergeSorted = mergeSort(deepcopy(listToSort))
		insertionSorted = insertionSort(deepcopy(listToSort))
		print("Merge Sorted list:\r\n{}\r\n".format(mergeSorted))
		print("Insertion Sorted list:\r\n{}\r\n".format(insertionSorted))
		print("Lists equal? {}\r\n".format(mergeSorted == insertionSorted))
