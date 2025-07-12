import joblib
import numpy as np

# Load the trained model and scaler
MODEL_PATH = r"C:\Users\mohdf\network-ids\static\models\ids_model.pkl"
SCALER_PATH = r"C:\Users\mohdf\network-ids\static\models\scaler.pkl"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Print model attack type mapping
attack_mapping = {
    0: "Normal",
    1: "DDoS",
    2: "Port Scan",
    3: "Brute Force",
    4: "Web Attack",
    5: "Botnet",
    6: "Infiltration",
    7: "Malware",
    8: "Data Theft",
    9: "DoS",
    10: "Backdoor",
    11: "MITM Attack",
    12: "Privilege Escalation",
    13: "Phishing",
    14: "Trojan"
}

print("✅ Model Attack Type Mapping:")
for label, attack in attack_mapping.items():
    print(f"{label}: {attack}")

# Define a sample attack feature set (Modify if needed)
attack_sample = np.random.rand(1, 78)  # Random values simulating attack traffic

# Scale the features
attack_sample = scaler.transform(attack_sample)

# Perform prediction
prediction = model.predict(attack_sample)[0]
attack_type = attack_mapping.get(int(prediction), "Unknown Threat")

print(f"🔍 Model Predicted: {prediction} ({attack_type})")
