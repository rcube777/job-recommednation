import joblib
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import os


df1=pd.read_csv('C:/Users/LENOVO/Desktop/JRS/back/jrs-django/match/data/dice_com-job_us_sample.csv')
df1.head()
df1.info()
df1=df1.dropna()
df1.shape
df1['jobdescription'].head()

tfidf_vectorizer_loaded = joblib.load('C:/Users/LENOVO/Desktop/JRS/back/algos/model.pkl')


def use(title, jobType, skills=[]):
    newData = title + ' ' +  jobType + ' ' + ' '.join(skills)
    input_matrix = tfidf_vectorizer_loaded.transform([newData])

    loadedMatrix = joblib.load('C:/Users/LENOVO/Desktop/JRS/back/algos/store.bin')

    # Calculate cosine similarities between the new data and existing job descriptions
    cosine_similarities = linear_kernel(input_matrix, loadedMatrix).flatten()

    # Get indices of most similar job descriptions
    similar_indices = cosine_similarities.argsort()[:-11:-1]

    recommended = []
    recommended = df1.iloc[similar_indices].to_dict()

    return recommended


