# Euclid GCD Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(log n * (log m + log n) ^ 2)
# python euclid.py 5 15

# imports
import sys
import math

# modular exponentiation
def euclid(x, y):
	if (x < y):
		t = x
		x = y
		y = t
	ret = x
	if (y != 0):
		ret = euclid(y, x % y)
	return ret

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print("\r\nEuclid GCD Algorithm by William M Mortl")
		print("Usage: python euclid.py {value1} {value2}")
		print("Example: python euclid.py 5 15\r\n")
	else:
		x = int(sys.argv[1])
		y = int(sys.argv[2])
		f = euclid(x, y)
		print(("\r\nGCD of %s and %s = %s\r\n") % (str(x), str(y), str(f)))
