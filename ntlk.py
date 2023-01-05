import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))
txt = "Avani, Vismaya and  are my good friends. " \
 \
      "Avani is getting married next year. " \
 \
      "Marriage is a big step in one’s life." \
 \
      "It is both exciting and frightening. "
tokenized = sent_tokenize(txt)
for i in tokenized:
    wordsList = nltk.word_tokenize(i)
    wordsList = [w for w in wordsList if not w in stop_words]
    tagged = nltk.pos_tag(wordsList)
    print(tagged)