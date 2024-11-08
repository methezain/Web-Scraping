import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import make_pipeline
import numpy as np

# Load the data from the JSON file
with open('/mnt/data/Final Data - Editing.json', 'r') as file:
    data = json.load(file)

# Extract summaries and relationships
summaries = [case['Summary'] for case in data if case['Summary'] != "No Summary Found for this case."]
relationships = [case['Relationship'] for case in data if case['Summary'] != "No Summary Found for this case."]
df = pd.DataFrame({'Summary': summaries, 'Relationship': relationships})

# Preprocess the labels
label_encoder = LabelEncoder()
df['Label'] = label_encoder.fit_transform(df['Relationship'])

# Split the data into training and testing sets
train_texts, val_texts, train_labels, val_labels = train_test_split(
    df['Summary'], df['Label'], test_size=0.2, random_state=42
)

# Create a pipeline with TF-IDF Vectorizer and Logistic Regression
pipeline = make_pipeline(
    TfidfVectorizer(stop_words='english', max_features=5000),
    LogisticRegression(max_iter=1000)
)

# Train the model
pipeline.fit(train_texts, train_labels)

# Predict relationships for all summaries
all_summaries = [case['Summary'] for case in data]
predicted_labels = pipeline.predict(all_summaries)

# Replace the "Relationship" values in the JSON data
predicted_relationships = label_encoder.inverse_transform(predicted_labels)
for i, case in enumerate(data):
    case['Relationship'] = predicted_relationships[i]

# Save the updated JSON file
with open('Updated_Data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

print("Updated JSON file has been saved as 'Updated_Data.json'.")
