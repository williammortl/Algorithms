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
	if (N <= 1):
		return ("neither", 0)
	ret = "prime"
	if (N <= 4):
		numChecks = 2
	else:
		numChecks = random.randint(2, N - 2)
	for i in range(1, numChecks):
		a = random.randint(1, N - 1)
		v = modularExponentiation.modularExponentiation(a, N - 1, N)
		if (v != 1):
			ret = "composite"
			break
	return (ret, i)

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nFermat's Little Theorem Primality Test Algorithm by William M Mortl")
		print("Usage: python fermatTest.py {value to test for primality}")
		print("Example: python fermatTest.py 5\r\n")
	else:
		N = int(sys.argv[1])
		(p, numChecks) = fermatTest(N)
		print(("\r\n%s is a %s number. %s checks were run.\r\n") % (str(N), p, str(numChecks)))
