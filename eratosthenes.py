# Sieve of Eratosthenes Algorithm
# Implemented by William M Mortl
# O(n^2)
# python eratosthenes.py 1000 primes.txt

# imports
from math import floor
import os
import sys

# Sieve of Eratosthenes Algorithm
def sieveEratosthenes(upperBound):
	NOTCHECKED = 0
	PRIME = 1
	COMPOSITE = 2
	sievePrimes = [0] * upperBound
	sievePrimes[0] = 2
	for i in range(1, upperBound):
		if (sievePrimes[i] == NOTCHECKED):
			sievePrimes[i] = PRIME
			val = i + 1
			indexesToChange = [((val * j) - 1) for j in range(2, int(floor(upperBound / val)) + 1)]
			for index in indexesToChange:
				sievePrimes[index] = COMPOSITE
	return sievePrimes

# Returns just the prime numbers from Sieve of Eratosthenes Algorithm
def eratosthenes(lowerBound, upperBound):
	PRIME = 1
	primes = []
	sievePrimes = sieveEratosthenes(upperBound)
	for i in range(lowerBound - 1, upperBound):
		if (sievePrimes[i] == PRIME):
			primes.append(i + 1)
	return primes

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nSieve of Eratosthenes Algorithm by William M Mortl")
		print("Usage: python eratosthenes.py {sieve up to this number} {OPTIONAL: filename}")
		print("Example: python eratosthenes.py 1000 primes.txt\r\n")
	else:
		upperBound = int(sys.argv[1])
		primes = eratosthenes(2, upperBound)
		
		# print primes
		print("\r\nPrimes:\r\n-------")
		for i in range(0, len(primes)):
			print(primes[i])
		print("")
		
		# write to file if a filename was passed
		if (len(sys.argv) == 3):
			fileName = sys.argv[2]
			with open(fileName, "w") as f:
				for i in range(0, len(primes)):
					f.write("%s\n" % str(primes[i]))
