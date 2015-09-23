# Prime Finding Algorithms
# Implemented by William M Mortl
# Coded for Python 2.7.9
# python findPrime.py 4

# imports
from eratosthenes import eratosthenes
from math import pow
from millerRabin import millerRabin
from random import randint
import sys

# Prime Candidate Algorithm
def primeCandidate(digits):
	primeEnds = [1, 3, 7, 9]
	rangeFrom = int(pow(10, digits - 2))
	rangeTo = int(pow(10, digits - 1)) - 1
	start = randint(rangeFrom, rangeTo)
	ending = primeEnds[randint(0, 3)]
	p = int(str(start) + str(ending))
	return p

# Prime Guessing Algorithm
def guessPrime(digits):
	foundPrime = False
	numTries = 0
	while (foundPrime == False):
		numTries += 1
		p = primeCandidate(digits)
		(testResult, numChecks) = millerRabin(p)
		if (testResult == "prime"):
			foundPrime = True
	return (p, numTries)

# select n primes
def sievePrimes(digits, n):
	rangeFrom = int(pow(10, digits - 1))
	rangeTo = int(pow(10, digits)) - 1
	primes = eratosthenes(rangeFrom, rangeTo)
	ret = []
	for i in range(0, n):
		r = randint(0, len(primes) - 1)
		ret.append(primes[r])
		del primes[r]
	return ret
	
# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nPrime Finding Algorithms by William M Mortl")
		print("Usage: python findPrime.py {# of digits for the prime}")
		print("Example: python findPrime.py 4\r\n")
	else:
		digits = int(sys.argv[1])
		if (digits < 2):
			print("\r\nMust be at least 2 digits\r\n")
		else:
			(p, numTries) = guessPrime(digits)
			print(("\r\nGuessed prime number: %s found in %s tries") % (str(p), str(numTries)))
			p = sievePrimes(digits, 1)
			print(("\r\nSieved prime number using Sieve of Eratosthenes: %s\r\n") % str(p[0]))
