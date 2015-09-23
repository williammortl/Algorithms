# Miller-Rabin Primality Test Algorithm
# Miller-Rabin Primality Test Algorithm Implemented by William M Mortl
# Coded for Python 2.7.9
# O(k * (log n) ^ 3)
# python millerRabin.py 5

# imports
from math import pow
from modularExponentiation import modularExponentiation
import sys
from random import randint

# Miller-Rabin primality checker, totalTests = 5 so there's a 
# 	1/(4^totalTests) = 1/1024 chance that we're wrong
def millerRabin(N, totalTests = 10):

	# initial tests
	if (N <= 1):
		return ("neither", 0)
	elif (N <= 3):
		return ("prime", 0)
	elif (N % 2 == 0):
		return ("composite", 0)
	elif ((N > 5) and (N % 5 == 0)):
		return ("composite", 0)

	# init vars, figure out d s.t. 2^s * d == n - 1
	r = 1
	while ((N - 1) % int(pow(2, r)) == 0):
		r += 1
	r -= 1
	d = (N - 1) / int(pow(2, r))

	# keep repeating test totalTests times
	for numTests in range(1, totalTests + 1):

		# init vars for the loop
		a = randint(2, N - 2)
		x = modularExponentiation(a, d, N)

		# keep checking
		if ((x != 1) and (x != N - 1)):
			isCandidate = False
			for i in range(1, r):
				x = modularExponentiation(x, 2, N)
				if (x == 1):
					return ("composite", numTests)
				elif (x == N - 1):
					isCandidate = True
					i = r
			if (isCandidate == False):
				return ("composite", numTests)
	return ("prime", numTests)

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nMiller-Rabin Primality Test Algorithm by William M Mortl")
		print("Usage: python millerRabin.py {value to test for primality}")
		print("Example: python millerRabin.py 5\r\n")
	else:
		N = int(sys.argv[1])
		(p, numChecks) = millerRabin(N)
		print(("\r\n%s is a %s number. %s checks were run.\r\n") % (str(N), p, str(numChecks)))
