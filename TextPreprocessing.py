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
    customStopwords = ["‘", "’"]
    allStopwords = stopwords.words() + word_tokenize(string.punctuation) + customStopwords
    return [w for w in tokens if not w in allStopwords]

def removeNumbers(sentence):
    return re.sub(r'\d+', '', sentence)

def parseSentence(sentence):
    return removeStopwords(removeNumbers(stemSentence(sentence)))


