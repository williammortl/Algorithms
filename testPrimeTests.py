# Prime Testing Test Program
# Implemented by William M Mortl

# imports
from fermatTest import fermatTest
from findPrime import primeCandidate
from millerRabin import millerRabin
from random import randint
import sys

# test numbers
n = int(input("\r\nHow many tests? "))
for i in range(0, n):
	disagreements = []
	candidate = primeCandidate(randint(1, 7))
	tf = fermatTest(candidate)
	tm = millerRabin(candidate)
	print("Tested: {}, match? {} - Fermat({}): {} | Miller-Rabin({}): {}".format(candidate, tf[0] == tm[0], tf[1], tf[0], tm[1], tm[0]))
	if ((tf[0] == tm[0]) == False):
		disagreements.append([candidate, tf[0], tm[0]])
print("\r\nDisagreements:")
print(disagreements)
print("")
