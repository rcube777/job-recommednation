from flask import Flask, render_template, request, redirect, url_for
import math
import pandas as pd

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

df1 = pd.read_csv('../data/dice_com-job_us_sample.csv')
df1['combined_text'] = df1['employmenttype_jobstatus'].fillna('') + ' ' + \
                      df1['jobdescription'].fillna('') + ' ' + \
                      df1['joblocation_address'].fillna('') + ' ' + \
                      df1['shift'].fillna('') + ' ' + \
                      df1['skills'].fillna('')

job_descriptions = []

for items in df1['combined_text']:
    word_tokens = word_tokenize(items)
    filteredWords = []
    for w in word_tokens:
        if w not in stop_words:
            filteredWords.append(w)

    job_descriptions.append(filteredWords.join())
    break

print(job_descriptions[0])

# # Dummy user data for demonstration
# users = {'user1': {'password': 'password123', 'firstname': 'John', 'lastname': 'Doe'}}

# # Convert job descriptions to lowercase
# job_descriptions_lower = [desc.lower() for desc in job_descriptions]

# def calculate_tf(term, document):
#     term_count = document.count(term)
#     total_terms = len(document)
#     return term_count / total_terms if total_terms > 0 else 0

# def calculate_idf(term, corpus):
#     document_count = sum(1 for doc in corpus if term in doc)
#     return math.log(len(corpus) / (document_count + 1))

# def calculate_tfidf(term, document, corpus):
#     tf = calculate_tf(term, document)
#     idf = calculate_idf(term, corpus)
#     return tf * idf

# def calculate_tfidf_vector(document, corpus):
#     unique_terms = set(term for doc in corpus for term in doc.split())
#     tfidf_vector = [calculate_tfidf(term, document, corpus) for term in unique_terms]
#     return tfidf_vector

# tfidf_matrix = [calculate_tfidf_vector(doc.split(), job_descriptions) for doc in job_descriptions]
# print(tfidf_matrix)

# def cosine_similarity(vec1, vec2):
#     dot_product = sum(a * b for a, b in zip(vec1, vec2))
#     magnitude_vec1 = math.sqrt(sum(a ** 2 for a in vec1))
#     magnitude_vec2 = math.sqrt(sum(b ** 2 for b in vec2))
#     return dot_product / (magnitude_vec1 * magnitude_vec2) if (magnitude_vec1 * magnitude_vec2) != 0 else 0

# def get_recommendations(user_skills, user_job_type):
#     # Combine user's skills and job type into a single document
#     user_profile = f"{user_skills} {user_job_type}"

#     # Convert to lowercase
#     user_profile_lower = user_profile.lower()

#     # Add user profile to job descriptions
#     documents = job_descriptions_lower + [user_profile_lower]

#     # TF-IDF Vectorization
#     unique_terms = set(term for doc in documents for term in doc.split())
#     tfidf_matrix = [calculate_tfidf_vector(doc.split(), documents) for doc in documents]

#     # Calculate cosine similarities
#     cosine_similarities = [cosine_similarity(tfidf_matrix[-1], vec) for vec in tfidf_matrix[:-1]]
#     job_indices = sorted(range(len(cosine_similarities)), key=lambda k: cosine_similarities[k], reverse=True)

#     # Get top 2 recommendations
#     recommendations = [job_descriptions[i] for i in job_indices[:10]]
#     return recommendations
