""" Analyzes the word frequencies in a book downloaded from Project Gutenberg 
Author Ziyi Lan"""

import string


def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	with open (file_name, "r") as myfile:
		data=myfile.read().replace('\n', '')
	indexone=data.find("*** START OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF HUCKLEBERRY FINN ***")
	indextwo=data.find("*** END OF THIS PROJECT GUTENBERG EBOOK THE ADVENTURES OF HUCKLEBERRY FINN ***")
	datatwo=data[indexone:indextwo]
	exclude = set(string.punctuation)
	s = ''.join(ch for ch in datatwo if ch not in exclude)
	word_string=s.lower()
	word_list=word_string.split()
	return word_list


def get_top_n_words(word_list):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""

	myDict = {}     #Create a dictionary to do word counting.
	for w in word_list:
	  if (myDict.has_key(w)):
	     myDict[w] = myDict[w] + 1
	  else:
	     myDict[w] = 1
	return myDict

n=100  "The top n words one wants to find"

content=get_word_list("pg32325.txt")
freq = get_top_n_words(content)
topfreq = sorted(freq.iteritems(), key=lambda x:-x[1])[:n]
for x in topfreq:
    print "{0}: {1}".format(*x)


