import nltk
nltk.download("punkt_tab")

text = "I am Arqam. This is my life. I don't need no money. As long as I can feel the beat"

sentences = nltk.sent_tokenize(text)
print(sentences)