# Word/Sentence/Paragraph Counter
# Implemented by William M Mortl
# python3 wordCount.py3 textFile.txt

# imports
from copy import deepcopy
import sys
import re

# get all counts
def wordSentenceParagraphCounts(textBuffer):
	cleanText = cleanseText(deepcopy(textBuffer))
	return [wordCount(cleanText), sentenceCount(cleanText), paragraphCount(cleanText), cleanText]

# cleanse string
def cleanseText(textBuffer):

	#check for final paragraph break, add if not found
	if (textBuffer[-1] != "\n"):
		textBuffer += "\n"

	# cleanup paragraph breaks
	textBuffer = textBuffer.replace(r"\r", "")
	textBuffer = re.sub(r"([^\n])\n([^\n])", r"\1 \2", textBuffer)
	textBuffer = re.sub(r"[\n]+", "\n", textBuffer)

	# remove unwanted characters
	textBuffer = re.sub(r"[!?]", ".", textBuffer)
	textBuffer = re.sub(r"\.+", ".", textBuffer)
	textBuffer = re.sub(r"[\"'()[\]{}/\`~@#$%^&$*+=,<>|:;]", "", textBuffer)
	textBuffer = re.sub(r"[\s]+\.", ".", textBuffer)

	# hyphen fixes
	textBuffer = re.sub(r"[-]+", r"-", textBuffer)
	textBuffer = re.sub(r"[\s]+-[\s]+", r" ", textBuffer)
	textBuffer = re.sub(r"-[\s]*[.]+", r".", textBuffer)

	# collapse repeated whitespace
	textBuffer = re.sub(r"[ \t]+", " ", textBuffer)
	textBuffer = re.sub(r"[ \t\n]+\.", ".", textBuffer)

	# generic abbreviation fixes
	before = 0
	after = len(textBuffer)
	while (before != after):
		before = len(textBuffer)
		textBuffer = re.sub(r"([a-zA-Z])\.([a-zA-Z])", r"\1\2", textBuffer)
		after = len(textBuffer)

	# specific abbreviation fixes
	textBuffer = re.sub(r"(Dr|Mr|Ms|Mrs|Drs|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\.", r"\1", textBuffer)

	return textBuffer

# word count
def wordCount(textBuffer):
	endOfParagraphCount = textBuffer.count("\n")
	spaceCount = textBuffer.count(" ")
	return endOfParagraphCount + spaceCount

# sentence count
def sentenceCount(textBuffer):
	return len(re.findall(r"\.( )*[A-Z\n]", textBuffer))

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
		
		# load file
		fileName = sys.argv[1]
		with open(fileName, "r") as f:
			textBuffer = f.read()

		# cleanse and parse
		[wCount, sCount, pCount, cleanText] = wordSentenceParagraphCounts(textBuffer)

		# output
		print("\r\nCLEANSED TEXT: \r\n")
		print(cleanText)
		print(("\r\nRESULTS: \r\n\r\nParagraphs: %s, Sentences: %s, Words: %s\r\n") %(pCount, sCount, wCount))