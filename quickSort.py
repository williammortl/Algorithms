# Quick Sort Algorithm
# Implemented by William M Mortl

# imports
import sys
from random import randint
import mergeSort

# in place quick sort function, quick sort range [i, j]
def quickSort(list, i, j):
	k = j - i
	if (k == 1):
		if (list[i] > list[j]):
			tmp = list[i]
			list[i] = list[j]
			list[j] = tmp
	elif (k > 1):
		i0 = i
		p = randint(i, j)
		tmp = list[j]
		list[j] = list[p]
		list[p] = tmp
		p = j
		while (i < p):
			if (list[i] >= list[p]):
				tmp = list[i]
				list[i : p] = list[(i + 1) : (p + 1)]
				list[p] = tmp
				p = p - 1
			else:
				i = i + 1
		quickSort(list, i0, p - 1)
		quickSort(list, p + 1, j)
	return list

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nQuick Sort by William M Mortl")
		print("Usage: python quickSort.py \"{comma seperated list of values to sort}\"")
		print("Example: python quickSort.py \"9,111,2,31,1,0\"\r\n")
	else:
		listToSort = map(int, sys.argv[1].split(","))
		print("\r\nSorting: " + str(listToSort))
		mergeSorted = mergeSort.mergeSort(listToSort)
		quickSorted = quickSort(listToSort, 0, len(listToSort) - 1)
		print("Merge Sorted list: " + str(mergeSorted))
		print("Quick Sorted list: " + str(quickSorted))
		print("Lists equal? " + str(mergeSorted == quickSorted) + "\r\n") 
