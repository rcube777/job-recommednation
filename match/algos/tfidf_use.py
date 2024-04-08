from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import pandas as pd

with open('store.bin', 'rb') as f:
    savedTfidf_matrix = pickle.load(f)


# cosine_sim=linear_kernel(savedTfidf_matrix,savedTfidf_matrix)

# tdif = TfidfVectorizer(stop_words='english')

# dd = []
# def get_recommendation(title, skills=[], cosine_sim=cosine_sim):
#     input_text = title + ' ' + ' '.join(skills)

#     input_matrix = tdif.fit_transform([input_text])

#     cosine_similarities = linear_kernel(input_matrix, savedTfidf_matrix).flatten()

#     similar_indices = cosine_similarities.argsort()[:-16:-1]

#     dd = df1.iloc[similar_indices].to_dict()

#     return dd

# recommended = get_recommendation('Ruby on Rails Developer', ['Javascript', 'Java', 'css'])

# data = []
# for key in recommended['jobtitle'].keys():
#     data.append([recommended['jobtitle'][key], recommended['joblocation_address'][key], recommended['skills'][key]])

# for jobs in data:
#     print(jobs)