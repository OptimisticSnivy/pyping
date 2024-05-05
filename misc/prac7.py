import nltk
import math
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

doc = "The sun shone brightly in the clear blue sky as birds chirped cheerfully among the lush green trees. The gentle breeze rustled the leaves, creating a soothing melody that filled the air with tranquility"

# Tokenization
tokens = word_tokenize(doc)
print(tokens)

# POS tagging
stop_words = set(stopwords.words('english'))
fil_tokens = [word for word in tokens if word.lower() not in stop_words]
print(fil_tokens)

# Stemming 
stemmer = PorterStemmer()
stem_tokens = [stemmer.stem(word) for word in fil_tokens]
print(stem_tokens)

# Lemmatizing 
lemmer = WordNetLemmatizer()
lem_tokens = [lemmer.lemmatize(word) for word in fil_tokens]
print(lem_tokens)

# Create representation using TF
tfidf_vect = TfidfVectorizer()
tfidf_matrix = tfidf_vect.fit_transform([''.join(lem_tokens)])

word = doc.split()

word_count = Counter(word)
total_words = len(word)
tf = {word: Count/total_words for word, Count in word_count.items()}

for word, tf_value in tf.items():
    print(f"{word}: {tf_value}")


# Create representation using TF
words = doc.split()
doc_containing_word = Counter()
for word in words:
    doc_containing_word[word] +=1

td = 1
idf = {word:math.log(td/count) for word,count in doc_containing_word}
for word, idf_value in idf.items():
    print(f"{word}: {idf_value}")
