import nltk
import string
from nltk import ngrams
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.corpus import gutenberg
from collections import Counter

#To compare other shakespeare's text, just change the file name.
file = open("Shakespeare Poetry.txt","r")
shake_poetry = file.read().lower()
file2 = open("Francis Bacon.txt","r")
bacon = file2.read().lower()



def tokenizing(file):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(file)
    return tokens


tokens_shake = tokenizing(shake_poetry)
sp_tokens = [s for s in tokens_shake if not s in stopwords.words('english')]
tokens_bacon = tokenizing(bacon)
bacon_tokens = [b for b in tokens_bacon if not b in stopwords.words('english')]
milton = tokenizing(gutenberg.raw('milton-paradise.txt'))
milton_tokens = [m for m in milton if not m in stopwords.words('english')]


#unigram and bigram
#Change the number 1 into 2 in order to figure out bigram result.

poe_grams = list(ngrams(sp_tokens, 1))
bacon_grams = list(ngrams(bacon_tokens, 1))
milton_grams = list(ngrams(milton_tokens, 1))

a = len(poe_grams)
b = len(bacon_grams)
c = len(milton_grams)
d = len(set.intersection(set(poe_grams), set(bacon_grams)))
e = len(set.intersection(set(poe_grams), set(milton_grams)))
# print(a,b,c,d,e,(d/a)*100, (d/b)*100, (e/a)*100, (e/c)*100)

#frequency
poe_freq = nltk.FreqDist(poe_grams)
bacon_freq = nltk.FreqDist(bacon_grams)
# print(poe_freq.most_common(10))
# print(bacon_freq.most_common(10))

#hapaxes legomenon
shake_hpl = (poe_freq.hapaxes())
bacon_hpl = (bacon_freq.hapaxes())
# print(len(shake_hpl))
# print(len(bacon_hpl))


def common_hapaxs(list1, list2):
    result = []
    for hapax in list1:
        if hapax in list2:
            result.append(hapax)
    return result
# print(common_hapaxs(shake_hpl,bacon_hpl))
# print(len(common_hapaxs(shake_hpl,bacon_hpl)))


#Shakespearen words
Bacon = open('Francis Bacon.txt', 'r')
Baconfile = Bacon.read()
BaconFile = Baconfile.split('.')
newBaconFile = []
for i in BaconFile:
    clean = i.replace('\n','')
    out = clean.strip(string.punctuation)
    newBaconFile.append(out.lower())

poetry = open('Shakespeare Poetry.txt', 'r')
poetryfile = poetry.readlines()
newPoetry = []
for i in poetryfile:
    clean = i.replace('\n','')
    out = clean.strip(string.punctuation)
    newPoetry.append(out.lower())
# print(newPoetry)

words = open("Shakespeare Words.txt", 'r',)
wordfile = words.readlines()
newWordFile = []
for i in wordfile:
    clean = i.replace('\n', '')
    out = clean.strip(string.punctuation)
    newWordFile.append(clean)
# print(newWordFile)

common_bacon_sentence = []
common_bacon_word = []
for baconword in newWordFile:
    for baconsentence in newBaconFile:
        if baconword in baconsentence:
            common_bacon_sentence.append(baconsentence)
            if baconword not in common_bacon_word:
                common_bacon_word.append(baconword)
# print(common_bacon_sentence)
# print(common_bacon_word)
# print(len(common_bacon_word)) #18

#sentence Tagging
def sentence_Tagging(list):
    string = str(list)
    use = nltk.word_tokenize(string)
    pos = nltk.pos_tag(use)
    return pos

bacon_tags = sentence_Tagging(common_bacon_sentence)
# print(shake_tags)

common_poetry_sentence = []
common_poetry_word = []
for poetryword in newWordFile:
    for poetrysentence in newPoetry:
        if poetryword in poetrysentence:
            common_poetry_sentence.append(poetrysentence)
            if poetryword not in common_poetry_word:
                common_poetry_word.append(poetryword)
# print(common_poetry_sentence)
# print(common_poetry_word)
# print(len(common_poetry_word)) #42
shake_tags = sentence_Tagging(common_poetry_sentence)
# print(shake_tags)

#counting the pos tags and their proportion in each corpus
shake_counts = Counter(tag for word, tag in shake_tags)
bacon_counts = Counter(tags for words, tags in bacon_tags )
# print(shake_counts)
# print(bacon_counts)
shake_total = sum(shake_counts.values())
shake_portion = dict((word, float(count)/shake_total) for word,count in shake_counts.items())
bacon_total = sum(bacon_counts.values())
bacon_portion = dict((words, float(count)/bacon_total) for words,count in bacon_counts.items())

# print(shake_portion) top ten: NN WP$ NNS IN PRP$ VBP JJ MD PRP VB
# print(bacon_portion) top ten: JJ CC CD NN VBZ RBS MD VB DT IN