# Merge Sort Algorithm
# Implemented by William M Mortl

# imports
import sys

# merge function, both lists need to be sorted
def merge(list1, list2):
	output = [];
	list1Pointer = 0;
	list2Pointer = 0;
	while ((list1Pointer < len(list1)) or (list2Pointer < len(list2))):
		if (list1Pointer < len(list1)):
			if (list2Pointer < len(list2)):
				if (list1[list1Pointer] < list2[list2Pointer]):
					output.append(list1[list1Pointer])
					list1Pointer = list1Pointer + 1
				else:
					output.append(list2[list2Pointer])
					list2Pointer = list2Pointer + 1
			else:
				output.append(list1[list1Pointer])
				list1Pointer = list1Pointer + 1
		else:
			output.append(list2[list2Pointer])
			list2Pointer = list2Pointer + 1
	return output

# merge sort function
def mergeSort(listToSort):
	output = listToSort
	listLength = len(listToSort)
	if (listLength == 2):
		output = listToSort
		if (output[0] > output[1]):
			output.reverse()
	elif (listLength > 2):
		splitPoint = int(listLength / 2)
		leftList = mergeSort(listToSort[0 : splitPoint])
		rightList = mergeSort(listToSort[splitPoint : listLength])
		output = merge(leftList, rightList)
	return output

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nMerge Sort by William M Mortl")
		print("Usage: python mergeSort.py \"{comma seperated list of values to sort}\"")
		print("Example: python mergeSort.py \"9,111,2,31,1,0\"\r\n")
	else:
		listToSort = map(int, sys.argv[1].split(","))
		print("\r\nSorting: " + str(listToSort))
		print("Sorted list: " + str(mergeSort(listToSort)) + "\r\n")
		