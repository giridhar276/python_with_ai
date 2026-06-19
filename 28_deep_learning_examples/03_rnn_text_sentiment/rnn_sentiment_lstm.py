"""
RNN / LSTM Example
Use case: Text Sentiment Classification

Input file:
bank_reviews_sentiment.csv

Goal:
Classify customer reviews as positive or negative.
"""

import pandas as pd
from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Step 1: Load dataset
df = pd.read_csv("bank_reviews_sentiment.csv")

print(df.head())


# Step 2: Separate text and label
texts = df["review"].values
labels = df["sentiment"].values


# Step 3: Convert text into numbers using Tokenizer
tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)

sequences = tokenizer.texts_to_sequences(texts)


# Step 4: Pad sequences
max_length = 12

padded_sequences = pad_sequences(
    sequences,
    maxlen=max_length,
    padding="post",
    truncating="post"
)


# Step 5: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    padded_sequences,
    labels,
    test_size=0.2,
    random_state=42
)


# Step 6: Build RNN/LSTM model
model = Sequential([
    Embedding(input_dim=1000, output_dim=16, input_length=max_length),
    LSTM(32),
    Dense(16, activation="relu"),
    Dense(1, activation="sigmoid")
])


# Step 7: Compile model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


# Step 8: Train model
model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=8,
    validation_split=0.2
)


# Step 9: Evaluate model
loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)


# Step 10: Predict new review
new_review = ["the banking service was excellent and helpful"]

new_sequence = tokenizer.texts_to_sequences(new_review)
new_padded = pad_sequences(new_sequence, maxlen=max_length, padding="post")

prediction = model.predict(new_padded)

if prediction[0][0] > 0.5:
    print("Prediction: Positive sentiment")
else:
    print("Prediction: Negative sentiment")
