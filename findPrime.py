# Prime Finding Algorithms
# Implemented by William M Mortl
# Coded for Python 2.7.9
# python findPrime.py 4

# imports
from eratosthenes import eratosthenes
from fermatTest import fermatTest
from math import pow
import sys
from random import randint

# Prime Guessing Algorithm
def guessPrime(digits):
	primeEnds = [1, 3, 7, 9]
	rangeFrom = int(pow(10, digits - 2))
	rangeTo = int(pow(10, digits - 1)) - 1
	foundPrime = False
	numTries = 0
	while (foundPrime == False):
		start = randint(rangeFrom, rangeTo)
		ending = primeEnds[randint(0, 3)]
		p = int(str(start) + str(ending))
		(testResult, numChecks) = fermatTest(p)
		if (testResult == "prime"):
			foundPrime = True
		numTries += 1
	return (p, numTries)

# Pick prime using Sieve of Eratosthenes Algorithm
def pickPrime(digits):
	rangeFrom = int(pow(10, digits - 1))
	rangeTo = int(pow(10, digits)) - 1
	primes = eratosthenes(rangeFrom, rangeTo)
	return primes[randint(0, len(primes) - 1)]

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
			p = pickPrime(digits)
			print(("\r\nPicked prime number using Sieve of Eratosthenes: %s\r\n") % str(p))
