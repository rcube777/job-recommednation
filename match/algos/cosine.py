from sklearn.metrics.pairwise import cosine_similarity

# Assuming you have a dictionary where keys are sentences and values are their vectors
sentence_vector_dict = {
    "sentence1": [0.1, 0.2, 0.3, 0.4],
    "sentence2": [0.2, 0.3, 0.4, 0.5]
}

# Extract vectors from the dictionary
vectors = list(sentence_vector_dict.values())

# Compute cosine similarity
similarity_matrix = cosine_similarity(sentence_vector_dict['sentence1'], sentence_vector_dict['sentence2'])

# Print cosine similarity matrix
print("Cosine Similarity Matrix:")
print(similarity_matrix)
