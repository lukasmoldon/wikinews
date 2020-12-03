from nltk.stem import LancasterStemmer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import nltk
import string
import re
from wordfreq import zipf_frequency
from textblob import TextBlob


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

def wordfreq(word):
    return zipf_frequency(word,'en')


'''Possible tags according to https://medium.com/@gianpaul.r/tokenization-and-parts-of-speech-pos-tagging-in-pythons-nltk-library-2d30f70af13b
    CC coordinating conjunction
    CD cardinal digit
    DT determiner
    EX existential there (like: “there is” … think of it like “there exists”)
    FW foreign word
    IN preposition/subordinating conjunction
    JJ adjective ‘big’
    JJR adjective, comparative ‘bigger’
    JJS adjective, superlative ‘biggest’
    LS list marker 1)
    MD modal could, will
    NN noun, singular ‘desk’
    NNS noun plural ‘desks’
    NNP proper noun, singular ‘Harrison’
    NNPS proper noun, plural ‘Americans’
    PDT predeterminer ‘all the kids’
    POS possessive ending parent’s
    PRP personal pronoun I, he, she
    PRP$ possessive pronoun my, his, hers
    RB adverb very, silently,
    RBR adverb, comparative better
    RBS adverb, superlative best
    RP particle give up
    TO, to go ‘to’ the store.
    UH interjection, errrrrrrrm
    VB verb, base form take
    VBD verb, past tense took
    VBG verb, gerund/present participle taking
    VBN verb, past participle taken
    VBP verb, sing. present, non-3d take
    VBZ verb, 3rd person sing. present takes
    WDT wh-determiner which
    WP wh-pronoun who, what
    WP$ possessive wh-pronoun whose
    WRB wh-abverb where, when'''


def getNouns(words):
    nounTags = ["NN","NNS","NNP","NNPS","FW"]
    return tagWords(words, nounTags)
def getVerbs(words):
    verbTags = ["VBD","VBG","VBN","VBP","VBZ"]
    return tagWords(words,verbTags)
def tagWords(words, tags):
    txt = " ".join(words)
    tagged = nltk.pos_tag(nltk.word_tokenize(txt))
    if len(tags) == 0:
        #No filters given as input, return all words
        return tagged
    else:
        return [x[0] for x in tagged if x[1] in tags]