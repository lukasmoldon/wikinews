from nltk.stem import LancasterStemmer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import string
import re


stemmer = LancasterStemmer()
#stemmer = PorterStemmer()

def stemSentence(sentence):
    return stemmer.stem(sentence)

def removeStopwords(sentence):
    tokens = word_tokenize(sentence)
    customStopwords = ["‘", "’","-",".","”","“",'.',"new","said",'—']
    allStopwords = stopwords.words() + word_tokenize(string.punctuation) + customStopwords
    return [w for w in tokens if w not in allStopwords]

def removeNumbers(sentence):
    return re.sub(r'\d+', '', sentence)

def parseSentence(sentence):
    return removeStopwords(stemSentence(removeNumbers(sentence)))

