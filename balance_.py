import pandas as pd

# Load the dataset
df = pd.read_csv("C:/Users/mohdf/network-ids/Datasets/MachineLearningCVE/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv ")  # ✅ Replace with actual filename

# Strip spaces from column names (if not done earlier)
df.columns = df.columns.str.strip()

# Separate the two classes
df_ddos = df[df['Label'] == 'DDoS']
df_benign = df[df['Label'] == 'BENIGN']

# Undersample the DDoS class to match BENIGN class count
df_ddos_sampled = df_ddos.sample(n=len(df_benign), random_state=42)

# Combine both classes into a balanced dataset
df_balanced = pd.concat([df_benign, df_ddos_sampled])

# Shuffle the dataset
df_balanced = df_balanced.sample(frac=1, random_state=42).reset_index(drop=True)

# Save the balanced dataset
df_balanced.to_csv("balanced_dataset.csv", index=False)

# Print new class distribution
print("\nBalanced Class Distribution:")
print(df_balanced['Label'].value_counts())
