from pattern.web import *
import pickle

#----------------------------------------------------------------------------------------------------------------------------------
#import books chosen from Gutenberg database

oliver_twist_full_text = URL('http://gutenberg.pglaf.org/7/3/730/730.txt').download()
indexone=oliver_twist_full_text.find("*** START OF THIS PROJECT GUTENBERG EBOOK OLIVER TWIST ***")
indextwo=oliver_twist_full_text.find("*** END OF THIS PROJECT GUTENBERG EBOOK OLIVER TWIST ***")
oliver_twist=oliver_twist_full_text[indexone:indextwo]

great_expectation_full_text = URL('http://gutenberg.pglaf.org/1/4/0/1400/1400.txt').download()
indexthree=great_expectation_full_text.find("*** START OF THIS PROJECT GUTENBERG EBOOK GREAT EXPECTATIONS ***")
indexfour=great_expectation_full_text.find("*** END OF THIS PROJECT GUTENBERG EBOOK GREAT EXPECTATIONS ***")
great_expectation=great_expectation_full_text[indexthree:indexfour]


David_Copperfield_full_text = URL('http://gutenberg.pglaf.org/7/6/766/766.txt').download()
indexfive=David_Copperfield_full_text.find("*** START OF THIS PROJECT GUTENBERG EBOOK DAVID COPPERFIELD ***")
indexsix=David_Copperfield_full_text.find("*** END OF THIS PROJECT GUTENBERG EBOOK DAVID COPPERFIELD ***")
David_Copperfield=David_Copperfield_full_text[indexfive:indexsix]


Bleak_House_full_text = URL('http://gutenberg.pglaf.org/1/0/2/1023/1023.txt').download()
indexseven=Bleak_House_full_text.find("***START OF THE PROJECT GUTENBERG EBOOK BLEAK HOUSE***")
indexeight=Bleak_House_full_text.find("***END OF THE PROJECT GUTENBERG EBOOK BLEAK HOUSE***")
Bleak_House=Bleak_House_full_text[indexseven:indexeight]


A_TALE_OF_TWO_CITIES_full_text = URL('http://gutenberg.pglaf.org/9/98/98.txt').download()
indexnine=A_TALE_OF_TWO_CITIES_full_text.find("*** START OF THIS PROJECT GUTENBERG EBOOK A TALE OF TWO CITIES ***")
indexten=A_TALE_OF_TWO_CITIES_full_text.find("*** END OF THIS PROJECT GUTENBERG EBOOK A TALE OF TWO CITIES ***")
A_TALE_OF_TWO_CITIES=A_TALE_OF_TWO_CITIES_full_text[indexnine:indexten]

#----------------------------------------------------------------------------------------------------------------------------------


charles_dickens_texts=[oliver_twist,great_expectation,David_Copperfield,Bleak_House,A_TALE_OF_TWO_CITIES]



f = open('dickens_texts.pickle','w')
pickle.dump(charles_dickens_texts,f)
f.close()

