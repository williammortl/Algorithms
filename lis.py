# Longest Increasing Subsequence Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(n ^ 2)
# python lis.py "9,111,2,31,7,0,5,4,3,1,100001,32,31,27,16,15,999,3,3,3,3,100000000,7"

# imports
from copy import deepcopy
from lcs import longestCommonSubsequence
from mergeSort import mergeSort
import sys

# longest increasing subsequence, uses dynamic programming and memoization
def longestIncreasingSubsequence(list):
	return longestCommonSubsequence(list, mergeSort(deepcopy(list)))

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nLongest Increasing Subsequence Algorithm by William M Mortl")
		print("Usage: python lis.py \"{comma seperated list of values to search}\"")
		print("Example: python lis.py \"9,111,2,31,1,0\"\r\n")
	else:
		listToSearch = map(int, sys.argv[1].split(","))
		print(("\r\nSearch list:\r\n%s\r\n") % str(listToSearch))
		lis = longestIncreasingSubsequence(listToSearch)
		print(("Longest increasing subsequence:\r\n%s\r\n") % str(lis))