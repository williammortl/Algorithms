# Maximum Subarray Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(n log n)
# python maximumSubarray.py "-1,4,5,-1,-1,2,3,4,5,-4,-1,1"

# imports
from math import floor
import sys

# maximum subarray
def maximumSubarray(l, low, high):
	retVal = (low, high, sum(l[low:high + 1]))
	if (low < high):
		mid = int(floor((low + high) / 2))
		(left_low, left_high, left_sum) = maximumSubarray(l, low, mid)
		(right_low, right_high, right_sum) = maximumSubarray(l, mid + 1, high)
		(mid_low, mid_high, mid_sum) = maxCrossing(l, low, mid, high)
		if ((left_sum >= right_sum) and (left_sum >= mid_sum)):
			retVal = (left_low, left_high, left_sum)
		elif ((right_sum >= left_sum) and (right_sum >= mid_sum)):
			retVal = (right_low, right_high, right_sum)
		else:
			retVal = (mid_low, mid_high, mid_sum)
	return retVal

# max crossing subarray
def maxCrossing(l, low, mid, high):
	left_sum = 0
	right_sum = 0
	max_left = 0
	max_right = 0
	sum = 0
	for i in range(mid, low - 1, -1):
		sum += l[i]
		if (sum  > left_sum):
			left_sum = sum
			max_left = i
	sum = 0
	for i in range(mid + 1, high + 1, 1):
		sum += l[i]
		if (sum  > right_sum):
			right_sum = sum
			max_right = i
	return (max_left, max_right, left_sum + right_sum)

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nMaximum Subarray Algorithm by William M Mortl")
		print("Usage: python maximumSubarray.py \"{comma seperated list of numbers to analyze}\"")
		print("Example: python maximumSubarray.py \"-1,4,5,-1,-1,2,3,4,5,-4,-1,1\"\r\n")
	else:
		l = map(int, sys.argv[1].split(","))
		ms = maximumSubarray(l, 0, len(l) - 1)
		print("\r\nThe maximum subarray of:")
		print(("\r\n%s\r\n") % str(l))
		print("is:")
		print(("\r\n%s\r\n\r\nWhich sums to: %s\r\n") % (str(l[ms[0]:ms[1] + 1]), str(ms[2])))
