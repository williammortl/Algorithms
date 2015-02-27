# Longest Increasing Subsequence Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(n ^ 2)
# python lis.py "9,111,2,31,7,0,5,4,3,1,100001,32,31,27,16,15,999,3,3,3,3,100000000,7"

# imports
import copy
import sys

# longest increasing subsequence, uses dynamic programming and memoization
def longestIncreasingSubsequence(list):
	s = len(list)
	searchResults = zero2dMatrix(s, s)
	longestStartingPoint = s - 1
	searchResults[longestStartingPoint][longestStartingPoint] = 1
	lis = []
	for i in xrange((s - 2), -1, -1):
		longestLength = 0
		for j in range((i + 1), s):
			if (list[i] <= list[j]):
				sumVal = sum(searchResults[j])
				if (sumVal > longestLength):
					longestStartingPoint = i;
					longestLength = sumVal + 1
					searchResults[i] = copy.deepcopy(searchResults[j])
					searchResults[i][i] = 1
	for j in range(0, s):
		if (searchResults[longestStartingPoint][j] == 1):
			lis.append(list[j])
	return lis

# create 2d matrix of zeros, have to create different sublists to avoid byref problems
def zero2dMatrix(rows, cols):
	output = []
	for i in range(0, rows):
		output.append([0] * cols)
	return output

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nLongest Increasing Subsequence Algorithm by William M Mortl")
		print("Usage: python lis.py \"{comma seperated list of values to search}\"")
		print("Example: python lis.py \"9,111,2,31,1,0\"\r\n")
	else:
		listToSearch = map(int, sys.argv[1].split(","))
		print(("\r\nSearch list:\r\n%s") % str(listToSearch))
		lis = longestIncreasingSubsequence(listToSearch)
		print(("Longest increasing subsequence:\r\n%s\r\n") % str(lis))