# Bubble Sort Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(n ^ 2)
# python bubbleSort.py "9,111,2,31,7,0,5,4,3,1,100001,32,31,27,16,15,999,3,3,3,3,100000000,7"

# imports
from copy import deepcopy
from mergeSort import mergeSort
import sys

# in place bubble sort
def bubbleSort(listToSort):
	for i in range(0, len(listToSort)):
		for j in range(0, (len(listToSort) - i - 1)):
			if (listToSort[j] > listToSort[j + 1]):
				tmp = listToSort[j]
				listToSort[j] = listToSort[j + 1]
				listToSort[j + 1] = tmp
	return listToSort

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nBubble Sort by William M Mortl")
		print("Usage: python bubbleSort.py \"{comma seperated list of values to sort}\"")
		print("Example: python bubbleSort.py \"9,111,2,31,1,0\"\r\n")
	else:
		listToSort = map(int, sys.argv[1].split(","))
		print(("\r\nSorting:\r\n%s\r\n") % str(listToSort))
		mergeSorted = mergeSort(deepcopy(listToSort))
		bubbleSorted = bubbleSort(deepcopy(listToSort))
		print(("Merge Sorted list:\r\n%s\r\n") % str(mergeSorted))
		print(("Bubble Sorted list:\r\n%s\r\n") % str(bubbleSorted))
		print(("Lists equal? %s\r\n") % str(mergeSorted == bubbleSorted))
