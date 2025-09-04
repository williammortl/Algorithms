# Read wordlist, the input word file should be a list of words, separated by line 
# 	breaks "\r\n", convert to DAG s.t. tan->rant, ran->rant, an->tan, an DOES NOT -> rant
# 	Prints out the three longest paths
# Implemented by William M Mortl

# imports
from copy import deepcopy
import sys

# size comparators
def wordSizeComparatorBigFirst(x, y):
	return len(y) - len(x)

def wordSizeComparatorSmallFirst(x, y):
	return len(x) - len(y)

# recurse through word
def recurseLongestPath(wordToCheck, dictionaries):

	# var init
	retLongestPath = []
	lenWord = len(wordToCheck)

	# check for base case
	if (lenWord == 1):
			dictionaries[0][wordToCheck][0] = 0
			dictionaries[0][wordToCheck][1] = []
	elif (lenWord > 1):
		if (dictionaries[lenWord - 1][wordToCheck][0] >= 0):
			retLongestPath = dictionaries[lenWord - 1][wordToCheck][1]
		elif (dictionaries[lenWord - 1][wordToCheck][0] == -1):

			# print word being analyzed
			print(("Analyzing word: %s") % wordToCheck)

			# current best path
			bestPath = []

			# loop through possible children words
			for charToDelete in range(0, lenWord):
				wordToCheckRecurse = wordToCheck
				if (charToDelete == 0):
					wordToCheckRecurse = wordToCheckRecurse[1:]
				elif (charToDelete == lenWord - 1):
					wordToCheckRecurse = wordToCheckRecurse[:(len(wordToCheckRecurse) - 1)]
				else:
					wordToCheckRecurse = wordToCheckRecurse[:charToDelete] + wordToCheckRecurse[(charToDelete + 1):]

				# check to see if child word exists
				if (wordToCheckRecurse in dictionaries[lenWord - 2]):
					pathToCheck = recurseLongestPath(wordToCheckRecurse, dictionaries)
					pathToCheck.append(wordToCheckRecurse)
					pathToCheck = list(set(pathToCheck))
					pathToCheck = sorted(pathToCheck, key=lambda x: len(x))

					# is this a longer best path
					if (len(pathToCheck) > len(bestPath)):
						bestPath = pathToCheck

			# save best path
			dictionaries[lenWord - 1][wordToCheck][0] = len(bestPath)
			dictionaries[lenWord - 1][wordToCheck][1] = bestPath
			retLongestPath = bestPath

	return deepcopy(retLongestPath)

# main entry point
if __name__ == "__main__":

	# read the file, eliminate duplicate words, eliminate sorted words
	fileName = input("\r\nWhich wordlist file? ")
	words = []
	with open(fileName, "r") as f:
		for line in f:
			line = line.replace("\n", "").upper()
			words.append(line)
	words = list(set(words))
	sortedWords = []
	sortedToWords = {}
	for word in words:
		sortedWord = ''.join(sorted(word))
		sortedWords.append(sortedWord)
		if (sortedWord in sortedToWords):
			sortedToWords[sortedWord].append(word)
		else:
			sortedToWords[sortedWord] = [word]
	sortedWords = list(set(sortedWords))

	# sort words by length (biggest first)
	sortedWords = sorted(sortedWords, key=lambda x: -len(x))
	maxLength = len(sortedWords[0])

	# create dictionaries
	sortedWordsDictionaries = []
	for i in range(0, maxLength):
		sortedWordsDictionaries.append({})
	for sortedWord in sortedWords:
		sortedWordsDictionaries[len(sortedWord) - 1][sortedWord] = [-1, []]

	# spin through words and build max paths in dictionary
	for sortedWord in sortedWords:
		path = recurseLongestPath(sortedWord, sortedWordsDictionaries)

	# spin through dictionaries find max path
	maxPaths = [[0,[]], [0,[]], [0,[]]]
	for sortedWord in sortedWords:
		lenPathWordToCheck = sortedWordsDictionaries[len(sortedWord) - 1][sortedWord][0]
		for path in maxPaths:
			if (lenPathWordToCheck > path[0]):
				path[0] = lenPathWordToCheck
				path[1] = str(sortedWord)
				break

	# print word path
	print("\r\n3 Max Word Paths:")
	for path in maxPaths:
		thePath = sortedWordsDictionaries[len(path[1]) - 1][path[1]][1]
		thePath = list(map(lambda x: sortedToWords[x], thePath))
		print("-----------------\r\n\r\nLength: {}\r\n".format(len(thePath) + 1))
		for word in thePath:
			print("Word(s): {}".format(word))
	print("Word(s): {}".format(sortedToWords[path[1]]))
	print("")
