import nltk

from sklearn.feature_extraction.text import CountVectorizer
from nltk.book import *
import re, pprint

f = open('mercadoLibre.txt','rU')
raw = f.read()
tokens = nltk.word_tokenize(raw)


text = nltk.Text(tokens)
fd = FreqDist(text)

print('TOKENS ', tokens[:10])
print('FREQUENCY DISTRIBUTION acondicionado', fd['acondicionado'])

# print('CONCORDANCE aire ',text.concordance('aire'))
# print('COLOCATIONS ', text.collocations())

labels = {
    'precio_final': 'no',
    # 'deuda': 'si',
    # 'unico_dueno': 'no',
    # 'aire': 'si',
    # 'alzacristales_electricos': 'si',
    # 'combustible': 'nafta'
}

labels['kilometraje'] = 158000
labels['cubiertas'] = 'nuevas'
print(labels)


lst = [w for w in tokens if re.search('t..o$', w)]
print('ENDINGS IN o :', lst)



def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document) [1]
    sentences = [nltk.word_tokenize(sent) for sent in sentences] [2]
    sentences = [nltk.pos_tag(sent) for sent in sentences] [3]


print( [w for w in tokens if re.search('[0-9]', w)] )
print( [w for w in tokens if re.search('[$][0-9]', w)] )

print( [w for w in tokens if re.search('^t.*o$', w)] )



# {}[]



