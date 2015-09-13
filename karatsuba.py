# Karatsuba Multiplication Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(n ^ log2 3)
# python karatsuba.py 13149 7913 10 3

# imports
import math
import sys

# Karatsuba Multiplication Algorithm
def karatsuba(x, y, B, m):
	c = int(math.pow(B, m))
	xm = int(math.floor(x / c))
	xr = x % c
	ym = int(math.floor(y / c))
	yr = y % c
	z2 = xm * ym
	z0 = xr * yr
	z1 = (xm + xr) * (ym + yr) - z2 - z0
	return z2 * int(math.pow(c, 2)) + z1 * c + z0

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 5):
		print("\r\nKaratsuba Multiplication Algorithm by William M Mortl")
		print("Usage: python karatsuba.py x y B m")
		print("Example: python karatsuba.py 13149 7913 10 3\r\n")
	else:
		x = int(sys.argv[1])
		y = int(sys.argv[2])
		B = int(sys.argv[3])
		m = int(sys.argv[4])
		v = karatsuba(x, y, B, m)
		vp = x * y
		print(("\r\nUsing Karatsuba: %s * %s = %s - verified against %s, %s\r\n") % (str(x), str(y), str(v), str(vp), str(v == vp)))
