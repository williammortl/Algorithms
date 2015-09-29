# Prime Testing Test Program
# Implemented by William M Mortl
# Coded for Python 2.7.9

# imports
from fermatTest import fermatTest
from findPrime import primeCandidate
from millerRabin import millerRabin
from random import randint
import sys

# test numbers
n = int(raw_input("\r\nHow many tests? "))
for i in range(0, n):
	disagreements = []
	candidate = primeCandidate(randint(1, 7))
	tf = fermatTest(candidate)
	tm = millerRabin(candidate)
	print(("Tested: %s, match? %s - Fermat(%s): %s | Miller-Rabin(%s): %s") % (str(candidate), str(tf[0] == tm[0]), str(tf[1]), str(tf[0]), str(tm[1]), tm[0]))
	if ((tf[0] == tm[0]) == False):
		disagreements.append([candidate, tf[0], tm[0]])
print("\r\nDisagreements:")
print(disagreements)
print("")
