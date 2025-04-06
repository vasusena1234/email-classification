import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Read dataset from mounted artifact folder
data_path = os.path.join("/app/data", "spam.csv")
df = pd.read_csv(data_path, encoding='latin-1')

# Rename and clean
df = df.rename(columns={
    df.columns[0]: "label",
    df.columns[1]: "message"
})[["label", "message"]]

df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Split and train
X_train, X_test, y_train = train_test_split(df["message"], df["label"], test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])
pipeline.fit(X_train, y_train)

# Save model to output folder
os.makedirs("/app/model", exist_ok=True)
joblib.dump(pipeline, "/app/model/spam_classifier.pkl")
