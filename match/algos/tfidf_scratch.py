import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

df1=pd.read_csv('../data/dice_com-job_us_sample.csv')
df1.head()
df1.info()
df1=df1.dropna()
df1.shape
df1['jobdescription'].head()


df1['combined_text'] = df1['employmenttype_jobstatus'] + ' ' + df1['jobdescription'] + ' ' + df1['joblocation_address'] + df1['shift'] + ' ' + df1['skills']
tdif = TfidfVectorizer(stop_words='english')
df1['combined_text']=df1['combined_text'].fillna('')

def calculate_tf(term, document):
    term_count = document.count(term)
    total_terms = len(document)
    return term_count / total_terms if total_terms > 0 else 0

def calculate_idf(term, corpus):
    document_count = sum(1 for doc in corpus if term in doc)
    return math.log(len(corpus) / (document_count + 1))

def calculate_tfidf(term, document, corpus):
    tf = calculate_tf(term, document)
    idf = calculate_idf(term, corpus)
    return tf * idf

def calculate_tfidf_vector(document, corpus):
    unique_terms = set(term for doc in corpus for term in doc.split())
    tfidf_vector = [calculate_tfidf(term, document, corpus) for term in unique_terms]
    return tfidf_vector

# tdif_matrix = tdif.fit_transform(df1['combined_text'])
# tdif_matrix.shape

# joblib.dump(tdif, 'model.pkl')

# with open('store.bin', 'wb') as f:
#     pickle.dump(tdif_matrix, f)