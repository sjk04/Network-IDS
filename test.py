import joblib

# Load model and scaler
MODEL_PATH = r"C:\Users\mohdf\network-ids\static\models\ids_model.pkl"
SCALER_PATH = r"C:\Users\mohdf\network-ids\static\models\scaler.pkl"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Get expected features
model_features = list(scaler.feature_names_in_)

print("\n✅ Model expects these features:")
for feature in model_features:
    print(feature)
