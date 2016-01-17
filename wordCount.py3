# Word/Sentence/Paragraph Counter
# Implemented by William M Mortl
# Coded for Python 3.5.1
# python3 wordCount.py3 textFile.txt

# imports
import sys
import re

# cleanse string, \n at new paragraph ONLY
def loadAndCleanse(fileName):

	# load
	with open(fileName, "r") as f:
		textBuffer = f.read()

	# cleanup paragraph breaks
	textBuffer = textBuffer.replace("\r", "")
	textBuffer = re.sub("([^\n])(\n)([^\n])", r"\1 \3", textBuffer)
	textBuffer = re.sub("(\n)+", "\n", textBuffer)

	# collapse repeated spaces
	textBuffer = re.sub("( )+", " ", textBuffer)

	# remove unwanted characters
	textBuffer = re.sub("[!?]", ".", textBuffer)
	textBuffer = re.sub(r"\.+", ".", textBuffer)
	textBuffer = re.sub("[\"'()[\]{}/\`~@#$%^&*+=,<>|:]", "", textBuffer)
	
	# hyphen fixes
	textBuffer = textBuffer.replace(" - ", " ")
	textBuffer = re.sub("([0-9]+)(-)([0-9a-zA-Z]+)", r"\1 \3", textBuffer)
	
	return textBuffer

# word count
def wordCount(textBuffer):
	endOfParagraphCount = textBuffer.count("\n")
	spaceCount = textBuffer.count(" ")
	return endOfParagraphCount + spaceCount

# sentence count
def sentenceCount(textBuffer):
	semicolonCount = textBuffer.count(";")
	periodCount = len(re.findall("\. [A-Z\n]", textBuffer))
	return semicolonCount + periodCount

# paragraph count
def paragraphCount(textBuffer):
	return textBuffer.count("\n")

# main entry point
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("\r\nWord/Sentence/Paragraph Counter by William M Mortl")
		print("Usage: python3 wordCount.py3 {text file to parse}")
		print("Example: python3 wordCount.py3 textFile.txt\r\n")
	else:
		fileName = sys.argv[1]
		textBuffer = loadAndCleanse(fileName)
		wCount = wordCount(textBuffer)
		sCount = sentenceCount(textBuffer)
		pCount = paragraphCount(textBuffer)
		print("\r\nCLEANSED TEXT: \r\n")
		print(textBuffer)
		print(("\r\nRESULTS: \r\n\r\nParagraphs: %s, Sentences: %s, Words: %s\r\n") %(pCount, sCount, wCount))