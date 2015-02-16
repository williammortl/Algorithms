# Insertion Sort Algorithm
# Implemented by William M Mortl

# imports
import sys
import mergeSort

# in place insertion sort
def insertionSort(list):
	itr = 1
	while(itr < len(list)):
		valInsert = list[itr]
		for i in xrange((itr - 1), -1, -1):
			valCompare = list[i]
			if (valCompare < valInsert):
				list[(i + 2) : (itr + 1)] = list[(i + 1): (itr)]
				list[i + 1] = valInsert;
				break
			elif ((i == 0) and (valCompare > valInsert)):
				list[1 : (itr + 1)] = list[i : itr]
				list[i] = valInsert;
		itr = itr + 1
	return list

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nInsertion Sort by William M Mortl")
		print("Usage: python insertionsSort.py \"{comma seperated list of values to sort}\"")
		print("Example: python insertionsSort.py \"9,111,2,31,1,0\"\r\n")
	else:
		listToSort = map(int, sys.argv[1].split(","))
		print(("\r\nSorting:\r\n%s") % str(listToSort))
		mergeSorted = mergeSort.mergeSort(listToSort)
		insertionSorted = insertionSort(listToSort)
		print(("Merge Sorted list:\r\n%s") % str(mergeSorted))
		print(("Insertion Sorted list:\r\n%s") % str(insertionSorted))
		print(("Lists equal? %s\r\n") % str(mergeSorted == insertionSorted))
