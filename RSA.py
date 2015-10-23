# RSA Key-Finding & Encryption/Decryption Algorithms
# Implemented by William M Mortl
# Coded for Python 2.7.9
# python RSA.py 3 "1001, 43, 67, 6, 104, 10987, 777"

# imports
from copy import deepcopy
from euclid import euclid
from euclid import extEuclid
from findPrime import guessPrime
import math
from modularExponentiation import modularExponentiation
from random import randint
import sys

# generate public and private keys from primes p and q
def generateKeys(p, q):
	e = -1
	d = -1
	n = p * q
	totient = (p -1) * (q - 1)
	
	# get a public key prime number e s.t. e in [3, totient)
	# 	and gcd(e, totient) = 1
	e = 0
	while ((e < 3) or (e >= totient) or (euclid(e, totient) != 1)):
		digits = randint(len(str(p)), len(str(totient)))
		(e, tries) = guessPrime(digits)

	# get a private key prime number s.t. e * d = 1 mod totient 
	(xp, yp, factor) = extEuclid(e, totient)
	d = yp % totient

	return (e, d, n, totient)

# RSA crypt
def crypt(data, key, n):
	dataOut = deepcopy(data)
	for i in range(0, len(dataOut)):
		dataOut[i] = modularExponentiation(dataOut[i], key, n)
	return dataOut

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print("\r\nRSA Algorithms by William M Mortl")
		print("Usage: python RSA.py {digits in p & q} \"{comma seperated list of numbers to encrypt}\"")
		print("Example: python RSA.py 3 \"1001, 43, 67, 6, 104, 10987, 777\"\r\n")
	else:
		digits = int(sys.argv[1])
		m = map(long, sys.argv[2].split(","))
		print("\r\nSelecting p and q...\r\n")
		(p, tries) = guessPrime(digits)
		(q, tries) = guessPrime(digits)
		print(("p: %s") % str(p))
		print(("q: %s\r\n") % str(q))
		print("Generating keys...\r\n")
		(e, d, n, totient) = generateKeys(p, q)
		print(("Public key: %s") % str(e))
		print(("Private key: %s") % str(d))
		print(("n: %s") % str(n))
		print(("Totient: %s\r\n") % str(totient))
		print("Encrypting & Decrypting...\r\n")
		c = crypt(m, e, n)
		mp = crypt(c, d, n)
		print(("Original: %s") % str(m))
		print(("Encrypted: %s") % str(c))
		print(("Decrypted: %s\r\n") % str(mp))
		print(("Same? %s\r\n") % str(m == mp))
