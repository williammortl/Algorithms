# Division Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(n ^ 2)
# python division.py 49 7

# imports
import sys
import math

# division algorithm
def division(x, y):
	q = 0
	r = 0
	if (x != 0):
		(q, r) = division(int(math.floor(x / 2)), y)
		q = 2 * q
		r = 2 * r
		if (x % 2 != 0):
			r = r + 1
		if (r >= y):
			r = r - y
			q = q + 1
	return (q, r)

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print("\r\nDivision Algorithm by William M Mortl")
		print("Usage: python division.py {dividend} {divisor}")
		print("Example: python division.py 49 7\r\n")
	else:
		x = int(sys.argv[1])
		y = int(sys.argv[2])
		(q, r) = division(x, y)
		print(("\r\nDivision Algorithm (%s, %s) - standard (%s, %s)\r\n") % (str(q), str(r), str(x / y), str(x % y)))
