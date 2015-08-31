# Fermat's Little Theorem Primality Test Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(log n * (log m + log n) ^ 2)
# python fermatTest.py 5

# imports
import sys
import math
import modularExponentiation
import random

# Fermat's little theorem primality checker
def fermatTest(N):
	ret = "composite"
	a = random.randint(1, N - 1)
	v = modularExponentiation.modularExponentiation(a, N - 1, N)
	if (v == 1):
		ret = "prime"
	return ret

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nFermat's Little Theorem Primality Test Algorithm by William M Mortl")
		print("Usage: python fermatTest.py {value1} {value2}")
		print("Example: python fermatTest.py 5\r\n")
	else:
		N = int(sys.argv[1])
		p = fermatTest(N)
		print(("\r\nIs %s prime according to Fermat's little theorem? %s\r\n") % (str(N), str(p)))
