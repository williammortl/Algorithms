# Euclid GCD Algorithms
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(log n * (log m + log n) ^ 2)
# python euclid.py 15 5

# imports
from math import floor
import sys

# euclid factorizing algorithm
def euclid(x, y):
	if (x < y):
		t = x
		x = y
		y = t
	ret = x
	if (y > 0):
		ret = euclid(y, x % y)
	return ret

# extended euclid
def extEuclid(x, y):
	if (x < y):
		t = x
		x = y
		y = t
	ret = (1, 0, x)
	if (y > 0):
		(xp, yp, d) = extEuclid(y, x % y)
		ret = (yp, xp - int(floor(x / y)) * yp, d)
	return ret

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print("\r\nEuclid GCD Algorithms by William M Mortl")
		print("Usage: python euclid.py {value1} {value2}")
		print("Example: python euclid.py 15 5\r\n")
	else:
		x = int(sys.argv[1])
		y = int(sys.argv[2])
		(xp, yp, factor) = extEuclid(x, y)
		print(("\r\nGCD of %s and %s = %s\r\n") % (str(x), str(y), str(factor)))
