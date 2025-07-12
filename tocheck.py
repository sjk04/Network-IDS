import pandas as pd  # ✅ Import pandas

df = pd.read_csv("C:/Users/mohdf/network-ids/Datasets/MachineLearningCVE/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")# ✅ Ensure the correct dataset file path
print(df['Label'].value_counts())  # ✅ Count occurrences of each attack type
