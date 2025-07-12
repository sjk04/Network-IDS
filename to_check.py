from sklearn.preprocessing import StandardScaler
import joblib
import pandas as pd

# Load dataset
df = pd.read_csv("scaled_dataset.csv")

# Scale the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df)

# Save scaler
joblib.dump(scaler, "scaler.pkl")
print("Scaler saved as scaler.pkl")
