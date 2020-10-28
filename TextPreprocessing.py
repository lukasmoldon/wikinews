from nltk.stem import LancasterStemmer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import string


stemmer = LancasterStemmer()
#stemmer = PorterStemmer()

def stemSentence(sentence):
    return stemmer.stem(sentence)

def removeStopwords(sentence):
    tokens = word_tokenize(sentence)
    return [w for w in tokens if not w in stopwords.words() and not w in string.punctuation and not w in ["’"]]

def parseSentence(sentence):
    return removeStopwords(stemSentence(sentence))
