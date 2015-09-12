# Sieve of Eratosthenes Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# O(n^2)
# python eratosthenes.py 1000 primes.txt

# imports
import sys
import math
import os

# Sieve of Eratosthenes Algorithm
def eratosthenes(upTo):
	NOTCHECKED = 0
	PRIME = 1
	COMPOSITE = 2
	primes = [0] * upTo
	primes[0] = 2
	for i in range(1, upTo):
		if (primes[i] == NOTCHECKED):
			primes[i] = PRIME
			val = i + 1
			indexesToChange = [((val * j) - 1) for j in range(2, int(math.floor(upTo / val)) + 1)]
			for index in indexesToChange:
				primes[index] = COMPOSITE
	return primes

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nSieve of Eratosthenes Algorithm by William M Mortl")
		print("Usage: python eratosthenes.py {sieve up to this number} {OPTIONAL: filename}")
		print("Example: python eratosthenes.py 1000 primes.txt\r\n")
	else:
		upTo = int(sys.argv[1])
		primes = eratosthenes(upTo)
		
		# print primes
		print("\r\nPrimes:\r\n-------")
		for i in range(0, len(primes)):
			if (primes[i] == 1):
				print(str(i + 1))
		
		# write to file if a filename was passed
		if (len(sys.argv) == 3):
			fileName = sys.argv[2]
			with open(fileName, "w") as f:
				for i in range(0, len(primes)):
					if (primes[i] == 1):
						f.write("%s\n" % str(i + 1))

