# Modular Exponentiation Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(n^3)
# python modularExponentiation.py 5 2 17

# imports
import math
import sys

# modular exponentiation x ^ y mod N
def modularExponentiation(x, y, N):
	x = long(x)
	y = long(y)
	N = long(N)
	retVal = long(1)
	if (y > 0):
		z = modularExponentiation(x, y / 2, N)
		retVal = z ** 2
		if (y % 2 != 0):
			retVal = retVal * x
		retVal = retVal % N
	return retVal

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 4):
		print("\r\nModular Exponentiation Algorithm by William M Mortl")
		print("Usage: python modularExponentiation.py {val} {to the power} {modulo}")
		print("Example: python modularExponentiation.py 5 2 17\r\n")
	else:
		x = long(sys.argv[1])
		y = long(sys.argv[2])
		N = long(sys.argv[3])
		v = modularExponentiation(x, y, N)
		print(("\r\n%s to the power %s modulo %s = %s\r\n") % (str(x), str(y), str(N), str(v)))
