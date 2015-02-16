# Bubble Sort Algorithm
# Implemented by William M Mortl

# imports
import sys
import mergeSort

# in place bubble sort
def bubbleSort(list):
	for i in range(0, len(list)):
		for j in range(0, (len(list) - i - 1)):
			if (list[j] > list[j + 1]):
				tmp = list[j]
				list[j] = list[j + 1]
				list[j + 1] = tmp
	return list

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nBubble Sort by William M Mortl")
		print("Usage: python bubbleSort.py \"{comma seperated list of values to sort}\"")
		print("Example: python bubbleSort.py \"9,111,2,31,1,0\"\r\n")
	else:
		listToSort = map(int, sys.argv[1].split(","))
		print(("\r\nSorting:\r\n%s") % str(listToSort))
		mergeSorted = mergeSort.mergeSort(listToSort)
		bubbleSorted = bubbleSort(listToSort)
		print(("Merge Sorted list:\r\n%s") % str(mergeSorted))
		print(("Bubble Sorted list:\r\n%s") % str(bubbleSorted))
		print(("Lists equal? %s\r\n") % str(mergeSorted == bubbleSorted))
