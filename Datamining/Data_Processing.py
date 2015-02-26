import Data_Fetching
import pickle
from pattern.en import *

#------------------------------------------------------------------------------------------
# Load data from a file (will be part of your data processing script)
input_file = open('dickens_texts.pickle','r')
reloaded_copy_of_texts = pickle.load(input_file)

#------------------------------------------------------------------------------------------
#This is the function that count the top 30 words in the text.

# def countWordFrequency(content):
#    myDict = {}
#    listWords = content.split(" ")
#    for w in listWords:
#       if (myDict.has_key(w)):
#          myDict[w] = myDict[w] + 1
#       else:
#          myDict[w] = 1
#    return myDict

# freq = countWordFrequency(reloaded_copy_of_texts[0])
# topfreq = sorted(freq.iteritems(), key=lambda x:-x[1])[:30]
# for x in topfreq:
#     print "{0}: {1}".format(*x)

#---------------------------------------------------------------------------------------------
# This sectoin prints out the sentimental level each text.

print sentiment(reloaded_copy_of_texts[0])
print sentiment(reloaded_copy_of_texts[1])
print sentiment(reloaded_copy_of_texts[2])
print sentiment(reloaded_copy_of_texts[3])
print sentiment(reloaded_copy_of_texts[4])