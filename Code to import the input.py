from nltk import pos_tag
from nltk.chunk import conlltags2tree
from nltk.tree import Tree
import nltk
import itertools
from nltk import ne_chunk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import *
import win32com.client as wincl
#import gui.py
speak = wincl.Dispatch("SAPI.SpVoice")


#a="Hello, Ram Hardik. Ayurveda, one of the oldest forms of medicine, practised anywhere in the world, originated in the Indus Valley Civilization, around 5000 BCE. Ayurveda is a Sanskrit term which means life-knowledge (Ayu-life, Veda – Knowledge). Although Ayurveda falls under alternate therapies, most medical practitioners have conceded that the use of certain plants and herbs, to cure diseases, are similar to that in allopathy, where herb and plant extracts are used. ."
#speak.Speak(a)

