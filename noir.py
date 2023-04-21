##from sentence_transformers import SentenceTransformer, util
##from sklearn.feature_extraction.text import CountVectorizer
##from sklearn.feature_extraction.text import TfidfVectorizer
##import re
##import numpy as np
import sqlite3

##model = SentenceTransformer('all-mpnet-base-v2')
##
##
##class Text_Model():
##
##    def __init__(self, model, ngram=(2, 2), vectorizer=CountVectorizer, similarity_metric=util.dot_score):
##        self.model = model
##        self._vectorizer = vectorizer(ngram_range=ngram)
##        self.similarity_metric = similarity_metric
##
##    def normalize(self, texts):
##
##        for i in range(len(texts)):
##            texts[i] = texts[i].lower()
##            texts[i] = re.sub(r'[^\w]', ' ', texts[i])
##
##        return texts
##
##    def texts_to_keys(self, text):  # array
##        X = self._vectorizer.fit_transform(self.normalize(text))
##        candidates = self._vectorizer.get_feature_names_out()
##
##        return candidates
##
##    def similarity(self, texts_block, text, mean=True):  # all arrays
##        embedding = self.model.encode(self.normalize(texts_block))
##        candidate = self.model.encode(self.normalize(text))
##
##        distances = self.similarity_metric(candidate, embedding).numpy()
##
##        if mean:
##            distances = np.mean(distances, axis=1)
##
##        return distances
##
##
##tm = Text_Model(model)
con = sqlite3.connect('users.db')
cur = con.cursor()


def add_user(ident):
    ident = str(ident)
    cur.execute(f"INSERT into data values ({ident}, '[]', '[]', 0, '')")
    con.commit()

def recipients(post):
    result = []
    for data in cur.execute("SELECT user, liked, disliked FROM data"):
##        if 0.9 <= tm.similarity(data[1], post) < 0.5:
##            result.append(data[0])
        result.append(data[0])

    return result
##(un)muted to add
