import pandas as pd
import re
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import pickle

with open('static/model/tfidf_vectorizer.pickle', 'rb') as f:
    tfidf = pickle.load(f)
with open('static/model/model.pickle', 'rb') as f:
    model = pickle.load(f)


ps = PorterStemmer()
lem = WordNetLemmatizer()
def data_cleaning(text):
    review = re.sub('[^a-zA-Z]',' ' ,text)
    review = re.sub(r'https?:\/\/.*[\r\n]*',' ',review, flags=re.MULTILINE)
    review = review.lower()
    review = review.split()
    review = [lem.lemmatize(word) for word in review if word not in set(stopwords.words('english'))]
    review = " ".join(review)
    return model.predict(tfidf.transform([review]).toarray())[0]


