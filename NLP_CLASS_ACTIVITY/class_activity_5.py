from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ['playing', 'played', 'plays', 'running',
         'happily', 'studies', 'connected']

for word in words:
    print(word, "->", stemmer.stem(word))