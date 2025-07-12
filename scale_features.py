import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("balanced_dataset.csv")

# Drop 'Label' column
features = df.drop(columns=['Label'])

# Replace infinity with a large finite number (e.g., max of column)
for col in ['Flow Bytes/s', 'Flow Packets/s']:
    max_value = features[features[col] != np.inf][col].max()  # Max finite value
    features[col] = features[col].replace([np.inf, -np.inf], max_value)

# Cap extremely large values (e.g., >1e9)
for col in ['Flow Bytes/s', 'Flow Packets/s']:
    features[col] = np.where(features[col] > 1e9, 1e9, features[col])

# Scale features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Convert back to DataFrame
scaled_df = pd.DataFrame(scaled_features, columns=features.columns)

# Save cleaned dataset
scaled_df.to_csv("scaled_dataset.csv", index=False)
