import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')

text = "The boys are playing games."

lemmatizer = WordNetLemmatizer()
words = word_tokenize(text)

for word in words:
    print(word, "->", lemmatizer.lemmatize(word))