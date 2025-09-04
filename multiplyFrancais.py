# Multiply a la Francais Algorithm
# Implemented by William M Mortl
# O(n ^ 2)
# python multiplyFrancais.py 7 7

# imports
from math import floor
import sys

# multiply a la francais
def multiplyFrancais(x, y):
	ret = 0
	if (y != 0):
		z = multiplyFrancais(x, int(floor(y / 2)))
		ret = 2 * z
		if ((y % 2) != 0):
			ret = ret + x
	return ret

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print("\r\nMultiply a la Francais by William M Mortl")
		print("Usage: python multiplyFrancais.py {value 1} {value 2}")
		print("Example: python multiplyFrancais.py 7 7\r\n")
	else:
		x = int(sys.argv[1])
		y = int(sys.argv[2])
		m = multiplyFrancais(x, y)
		print(("\r\nMultiply a la Francais %s - standard %s\r\n") % (str(m), str(x * y)))
