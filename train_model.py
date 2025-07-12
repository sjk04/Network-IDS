import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import joblib

# Load scaled dataset
df = pd.read_csv("scaled_dataset.csv")

# Load labels separately
labels = pd.read_csv("balanced_dataset.csv")["Label"]

# Encode categorical labels into numerical values
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)

# Save the encoder for later use
joblib.dump(label_encoder, "label_encoder.pkl")

# Save feature column names for later use
joblib.dump(df.columns.tolist(), "feature_columns.pkl")

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(df, encoded_labels, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "ids_model.pkl")
print("Model saved as ids_model.pkl")
