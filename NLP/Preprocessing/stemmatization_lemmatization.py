import nltk
import string
from nltk.stem import PorterStemmer,WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = stopwords.words("english")

text = "Baby let me see, Jalebi Baby. I just wanna eat it. Oh, I really need it. I have been FLYING a lot lately and the Flights just keep getting DELAYED. Honestly, traveling for WORK gets exhausting with endless delays, but every trip teaches you something new!"
lower_text = text.lower()

tokens = nltk.word_tokenize(lower_text)
# print(tokens)

clean_tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]

stemmer = PorterStemmer()

stemmed = [stemmer.stem(word) for word in clean_tokens]

lemmatizer = WordNetLemmatizer()

lemmtized = [lemmatizer.lemmatize(word) for word in clean_tokens]

print(lemmtized)