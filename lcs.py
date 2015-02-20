# Longest Common Subsequence Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(n ^ 2)

# imports
import sys
import copy
import lis

# longest common subsequence, uses dynamic programming
def longestCommonSubsequence(list1, list2):
	s1 = len(list1)
	s2 = len(list2)
	results = lis.zero2dMatrix(s1 + 1, s2 + 1)
	for i in range(1, s1 + 1):
		for j in range(1, s2 + 1):
			if (list1[i - 1] == list2[j - 1]):
				results[i][j] = results[i - 1][j - 1] + 1
			elif (results[i - 1][j] >= results[i][j - 1]):
				results[i][j] = results[i - 1][j]
			else:
				results[i][j] = results[i][j - 1]
	return extractCommonSubsequence(results, list1)

# walks through the results matrix and extracts the longest common subsequence
def extractCommonSubsequence(results, rowList):
	lcs = []
	i = len(results) - 1
	j = len(results[0]) - 1
	while((i > 0) and (j > 0) and (results[i][j] > 0)):
		c = results[i][j]
		u = results[i - 1][j]
		l = results[i][j - 1]
		ul = results[i - 1][j - 1]
		if ((ul >= l) and (ul >= u) and (ul != c)):
			lcs.insert(0, rowList[i - 1])
			i = i - 1
			j = j - 1
		elif (u >= l):
			i = i -1
		else:
			j = j - 1
	return lcs

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print("\r\nLongest Common Subsequence Algorithm by William M Mortl")
		print("Usage: python lcs.py \"{comma seperated list of values to search}\" \"{comma seperated list of values to search}\"")
		print("Example: python lcs.py \"9,111,2,31,1,0\" \"9,7,111,2,31,6,7,6,1,4\"\r\n")
	else:
		list1 = map(int, sys.argv[1].split(","))
		list2 = map(int, sys.argv[2].split(","))
		print(("\r\nLooking for longest common subsequence of:\r\n%s\r\n%s") % (str(list1), str(list2)))
		lcs = longestCommonSubsequence(list1, list2)
		print(("Longest common subsequence:\r\n%s\r\n") % str(lcs))