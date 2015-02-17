# Longest Increasing Subsequence Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(n^2)

# imports
import sys
import copy

# longest increasing subsequence, uses dynamic programming
def longestIncreasingSubsequence(list):
	s = len(list)
	searchResults = zero2dMatrix(s)
	longestStartingPoint = s - 1
	searchResults[longestStartingPoint][longestStartingPoint] = 1
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
	lis = []
	for j in range(0, s):
		if (searchResults[longestStartingPoint][j] == 1):
			lis.append(list[j])
	return lis

# create 2d matrix of zeros, have to create different sublists to avoid byref problems
def zero2dMatrix(size):
	output = []
	for i in range(0, size):
		output.append([0] * size)
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