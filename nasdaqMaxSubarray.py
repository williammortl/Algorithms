# Read stock quotes from NASDAQ history files, find max subarrary
# Implemented by William M Mortl
# Coded for Python 2.7.9

# imports
from maximumSubarray import maximumSubarray
import os
import sys

# read CSV file
fileName = raw_input("\r\nWhich NASDAQ history CSV file? ")
print(fileName)
values = []
skip = True
with open(fileName, "r") as f:
	for line in f:
		if (skip == True):
			skip = False
		else:
			line = line.translate(None, "\"")
			fields = line.split(",")
			values.append(float(fields[1]))

# transform to diff
diff = [0]
for i in range(1, len(values)):
	diff.append(values[i] - values[i - 1])

# get max subarray
ms = maximumSubarray(diff, 0, len(diff) - 1)

# output
print("\r\nThe maximum subarray of:")
print(("\r\n%s\r\n") % str(diff))
print("is:")
print(("\r\n%s\r\n\r\nWhich sums to: %s\r\n") % (str(diff[ms[0]:ms[1] + 1]), str(ms[2])))
