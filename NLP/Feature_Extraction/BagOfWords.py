import nltk
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

stop_words = stopwords.words('english')

def preprocess(text):
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    tokens = [ word for word in tokens if word not in stop_words and word not in string.punctuation ]
    
    return " ".join(tokens)

