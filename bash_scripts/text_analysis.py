import nltk

locs = [('Omnicom', 'IN', 'New York'), ('DDB Needham', 'IN', 'New York'), ('Kaplan Thaler Group', 'IN', 'New York'), ('BBDO South', 'IN', 'Atlanta'), ('Georgia-Pacific', 'IN', 'Atlanta')]
query = [e1 for (e1, rel, e2) in locs if e2=='Atlanta']
print(query)

from sklearn.feature_extraction.text import CountVectorizer
from nltk.book import *

# text1.concordance("monstrous")
# fdist1 = FreqDist(text1)
# fdist1.most_common(20)

# from urllib import request
# url = "http://www.gutenberg.org/files/2554/2554.txt"
# url = "mercadoLibre.txt"
# response = request.urlopen(url)
# raw = response.read().decode('utf8')
# type(raw)
# len(raw)
# raw[:75]

f=open('mercadoLibre.txt','rU')
raw = f.read()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
fd = FreqDist(text)

print('FREQUENCY DISTRIBUTION acondicionado', fd['acondicionado'])
print('CONCORDANCE aire ',text.concordance('aire'))
print('COLOCATIONS ', text.collocations())

labels = {
    'precio_final': 'no',
    'deuda': 'si',
    'unico_dueno': 'no',
    'aire': 'si',
    'alzacristales_electricos': 'si',
    'combustible': 'nafta'
}

labels['kilometraje'] = 158000
labels['cubiertas'] = 'nuevas'
print(labels)

import nltk, re, pprint

def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document) [1]
    sentences = [nltk.word_tokenize(sent) for sent in sentences] [2]
    sentences = [nltk.pos_tag(sent) for sent in sentences] [3]


# {}[]