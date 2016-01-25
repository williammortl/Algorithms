# Word/Sentence/Paragraph Counter
# Implemented by William M Mortl
# Coded for Python 3.5.1
# python3 wordCount.py3 textFile.txt

# imports
import sys
import re

# cleanse string
def cleanseText(textBuffer):

	# cleanup paragraph breaks
	textBuffer = textBuffer.replace(r"\r", "")
	textBuffer = re.sub(r"([^\n])\n([^\n])", r"\1 \2", textBuffer)
	textBuffer = re.sub(r"(\n)+", "\n", textBuffer)

	# remove unwanted characters
	textBuffer = re.sub(r"[!?]", ".", textBuffer)
	textBuffer = re.sub(r"\.+", ".", textBuffer)
	textBuffer = re.sub(r"[\"'()[\]{}/\`~@#$%^&$*+=,<>|:;]", " ", textBuffer)
	
	# hyphen fixes
	textBuffer = textBuffer.replace(r" - ", " ")
	
	# collapse repeated spaces and tabs
	textBuffer = re.sub(r"[ \t]+", " ", textBuffer)
	
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
		textBuffer = cleanseText(textBuffer)
		wCount = wordCount(textBuffer)
		sCount = sentenceCount(textBuffer)
		pCount = paragraphCount(textBuffer)
		
		# output
		print("\r\nCLEANSED TEXT: \r\n")
		print(textBuffer)
		print(("\r\nRESULTS: \r\n\r\nParagraphs: %s, Sentences: %s, Words: %s\r\n") %(pCount, sCount, wCount))