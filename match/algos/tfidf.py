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

tdif_matrix = tdif.fit_transform(df1['combined_text'])
tdif_matrix.shape

joblib.dump(tdif, 'model.pkl')

with open('store.bin', 'wb') as f:
    pickle.dump(tdif_matrix, f)