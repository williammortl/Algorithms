# Read wordlist, the input word file should be a list of words, separated by line 
# 	breaks "\r\n", convert to DAG s.t. tan->rant, ran->rant, an->tan, an DOES NOT -> rant
# 	Prints out the three longest paths
# Implemented by William M Mortl
# Coded for Python 2.7.9

# imports
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
	if (lenWord > 1):
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
					pathToCheck.extend([wordToCheckRecurse])
					pathToCheck = list(set(pathToCheck))
					pathToCheck = sorted(pathToCheck, cmp = wordSizeComparatorSmallFirst)

					# is this a longer best path
					if (len(pathToCheck) > len(bestPath)):
						bestPath = pathToCheck

			# save best path
			dictionaries[lenWord - 1][wordToCheck][0] = len(bestPath)
			dictionaries[lenWord - 1][wordToCheck][1] = bestPath
			retLongestPath = bestPath

	return retLongestPath

# main entry point
if __name__ == "__main__":

	# read the file
	fileName = raw_input("\r\nWhich wordlist file? ")
	sortedWords = []
	sortedToWords = {}
	with open(fileName, "r") as f:
		for line in f:
			line = line.translate(None, "\n").upper()
			sortedWord = ''.join(sorted(line))
			sortedWords.append(sortedWord)
			if (sortedWord in sortedToWords):
				sortedToWords[sortedWord].append(line)
			else:
				sortedToWords[sortedWord] = [line]

	# remove duplicates from sortedWords
	sortedWords = list(set(sortedWords))

	# sort by length (biggest first)
	sortedWords = sorted(sortedWords, cmp = wordSizeComparatorBigFirst)
	maxLength = len(sortedWords[0])

	# create dictionaries
	sortedWordsDictionaries = []
	for i in range(0, maxLength):
		sortedWordsDictionaries.append({})
	for i in range(0, len(sortedWords)):
		sortedWordsDictionaries[len(sortedWords[i]) - 1][sortedWords[i]] = [-1, []]

	# spin through dictionaries and build max paths
	for i in range(0, len(sortedWords)):
		recurseLongestPath(sortedWords[i], sortedWordsDictionaries)

	# spin through dictionaries find max path
	max3Paths = [[0,[]], [0,[]], [0,[]]]
	for i in range(0, len(sortedWords)):
		wordToCheck = sortedWords[i]
		lenPathWordToCheck = sortedWordsDictionaries[len(wordToCheck) - 1][wordToCheck][0]
		for j in range(0, 3):
			if (lenPathWordToCheck > max3Paths[j][0]):
				max3Paths[j][0] = lenPathWordToCheck
				max3Paths[j][1] = wordToCheck
				break

	# print word path
	print("\r\n3 Max Word Paths:")
	for i in range(0, 3):
		maxPath = sortedWordsDictionaries[len(max3Paths[i][1]) - 1][max3Paths[i][1]][1]
		maxPath = map(lambda x: sortedToWords[x], maxPath)
		print(("-----------------\r\n\r\nLength: %s\r\n") % str(len(maxPath)))
		for j in range(0, len(maxPath)):
			print (("Word(s): %s") % str(maxPath[j]))
		print("")
