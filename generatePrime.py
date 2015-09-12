# Prime Generation Algorithm
# Implemented by William M Mortl
# Coded for Python 2.7.9
# python generatePrime.py 4

# imports
import sys
import random
import math
import fermatTest

# Prime Generation Algorithm
def generatePrime(digits):
	primeEnds = [1, 3, 7, 9]
	rangeFrom = int(math.pow(10, digits - 2))
	rangeTo = int(math.pow(10, digits - 1)) - 1
	foundPrime = False
	numTries = 0
	while (foundPrime == False):
		start = random.randint(rangeFrom, rangeTo)
		ending = primeEnds[random.randint(0, 3)]
		p = int(str(start) + str(ending))
		(testResult, numChecks) = fermatTest.fermatTest(p)
		if (testResult == "prime"):
			foundPrime = True
		numTries += 1
	return (p, numTries)

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nPrime Generation Algorithm by William M Mortl")
		print("Usage: python generatePrime.py {# of digits for the prime}")
		print("Example: python generatePrime.py 4\r\n")
	else:
		digits = int(sys.argv[1])
		if (digits < 2):
			print("\r\nMust be at least 2 digits\r\n")
		else:
			(p, numTries) = generatePrime(digits)
			print(("\r\nPrime number: %s found in %s tries\r\n") % (str(p), str(numTries)))

