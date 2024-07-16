import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load the spreadsheet
file_path = './is130.xlsx'
spreadsheet = pd.read_excel(file_path)

# Display the first few rows of the spreadsheet to understand its structure
print(spreadsheet.head())


# Isolate the questions and answers
questions_answers = spreadsheet[['Questions', 'Answers']]

# Total number of questions
total_questions = len(questions_answers)

print(total_questions)



# Calculate similarity between questions
vectorizer = TfidfVectorizer().fit_transform(questions_answers['Questions'])
vectors = vectorizer.toarray()
cosine_matrix = cosine_similarity(vectors)

# Set a threshold for similarity (0.8 is arbitrary and can be adjusted)
threshold = 0.8

# Find pairs of similar questions
similar_pairs = np.argwhere(cosine_matrix > threshold)
similar_pairs = similar_pairs[similar_pairs[:, 0] != similar_pairs[:, 1]]

# Create a set to hold unique indices of questions to keep
questions_to_keep = set(range(total_questions))

# Remove one of each pair of similar questions
for i, j in similar_pairs:
    if i in questions_to_keep and j in questions_to_keep:
        questions_to_keep.remove(j)

# Ensure the number of questions to keep is 90
while len(questions_to_keep) > 90:
    questions_to_keep.pop()

# Filter the questions and answers to keep only the selected questions
reduced_questions_answers = questions_answers.iloc[list(questions_to_keep)]

# Sort by index to maintain original order
reduced_questions_answers = reduced_questions_answers.sort_index()

# Display the first few rows of the reduced questions and answers
print(reduced_questions_answers.head(), len(reduced_questions_answers))


# Save the reduced questions and answers to a new Excel file
output_path = './Reduced_Questions_Answers.xlsx'
reduced_questions_answers.to_excel(output_path, index=False)

print(output_path)
