# app.py - Web-based Real-Time Intrusion Detection System (IDS) with Machine Learning
from flask import Flask, render_template, jsonify, request
import pandas as pd
import numpy as np
import time
import threading
import os
import joblib
from datetime import datetime
from collections import deque
from scapy.all import sniff, IP

app = Flask(__name__)

# Load trained model and scaler from static/model folder
MODEL_PATH = r"C:\Users\mohdf\network-ids\static\models\ids_model.pkl"
SCALER_PATH = r"C:\Users\mohdf\network-ids\static\models\scaler.pkl"
if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
    try:
        print(f"🔍 Loading model from: {MODEL_PATH}")
        print(f"🔍 Loading scaler from: {SCALER_PATH}")
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        print("✅ IDS Model and Scaler Loaded Successfully!")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        model, scaler = None, None
else:
    print("❌ Error: Model or Scaler not found at the specified path.")
    model, scaler = None, None

# Global variables to store detection results and statistics
alerts = deque(maxlen=100)
traffic_stats = {"total_packets": 0, "normal_packets": 0, "attack_packets": 0, "start_time": time.time()}
recent_traffic = deque(maxlen=300)
top_ips = {}
attack_types = {}

# Define attack categories
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

# Function to classify network traffic
def live_packet_capture(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        packet_size = len(packet)

        print(f"🔍 Packet Captured from {src_ip} → {dst_ip} | Protocol: {protocol} | Size: {packet_size}")

        # Extract features (ensure all expected features are included)
        features_dict = {
            "Destination Port": packet.dport if hasattr(packet, 'dport') else 0,
            "Flow Duration": 0,
            "Total Fwd Packets": 1,
            "Total Backward Packets": 0,
            "Total Length of Fwd Packets": packet_size,
            "Total Length of Bwd Packets": 0,
            "Fwd Packet Length Max": packet_size,
            "Fwd Packet Length Min": packet_size,
            "Fwd Packet Length Mean": packet_size,
            "Fwd Packet Length Std": 0,
            "Bwd Packet Length Max": 0,
            "Bwd Packet Length Min": 0,
            "Bwd Packet Length Mean": 0,
            "Bwd Packet Length Std": 0,
            "Flow Bytes/s": 0,
            "Flow Packets/s": 0,
            "Fwd Packets/s": 0,
            "Bwd Packets/s": 0,
            "Min Packet Length": packet_size,
            "Max Packet Length": packet_size,
            "Packet Length Mean": packet_size,
            "Packet Length Std": 0,
            "Packet Length Variance": 0,
            "FIN Flag Count": 0,
            "SYN Flag Count": 0,
            "RST Flag Count": 0,
            "PSH Flag Count": 0,
            "ACK Flag Count": 0,
            "URG Flag Count": 0,
            "CWE Flag Count": 0,
            "ECE Flag Count": 0,
            "Down/Up Ratio": 0,
            "Average Packet Size": 0,
            "Avg Fwd Segment Size": 0,
            "Avg Bwd Segment Size": 0,
            "Fwd Header Length.1": 0,
            "Fwd Avg Bytes/Bulk": 0,
            "Fwd Avg Packets/Bulk": 0,
            "Fwd Avg Bulk Rate": 0,
            "Bwd Avg Bytes/Bulk": 0,
            "Bwd Avg Packets/Bulk": 0,
            "Bwd Avg Bulk Rate": 0,
            "Subflow Fwd Packets": 0,
            "Subflow Fwd Bytes": 0,
            "Subflow Bwd Packets": 0,
            "Subflow Bwd Bytes": 0,
            "Init_Win_bytes_forward": 0,
            "Init_Win_bytes_backward": 0,
            "act_data_pkt_fwd": 0,
            "min_seg_size_forward": 0,
            "Active Mean": 0,
            "Active Std": 0,
            "Active Max": 0,
            "Active Min": 0,
            "Idle Mean": 0,
            "Idle Std": 0,
            "Idle Max": 0,
            "Idle Min": 0
        }

        # ✅ Ensure all required features exist in the correct order
        feature_names = scaler.feature_names_in_
        formatted_features = {feature: features_dict.get(feature, 0) for feature in feature_names}

        # Convert dictionary to DataFrame
        features_df = pd.DataFrame([formatted_features], columns=feature_names)

        # Debug: Print extracted features
        print("🛠️ Extracted Features for Prediction:")
        print(features_df)

        try:
            # Scale the features
            features_scaled = scaler.transform(features_df)

            # Perform prediction
            prediction = model.predict(features_scaled)[0]
            attack_type = attack_mapping.get(int(prediction), "Unknown Threat")

            status = "Attack" if prediction > 0 else "Normal"
            print(f"🔍 Raw Prediction Output: {prediction}")
            print(f"🔍 Mapped Attack Type: {attack_type}")


            print(f"🚀 [Real-Time] {src_ip} → {dst_ip} | Status: {status} | Attack Type: {attack_type}")

            # Update statistics
            traffic_stats["total_packets"] += 1

            if prediction > 0:
                traffic_stats["attack_packets"] += 1
                alerts.appendleft({
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "src_ip": src_ip,
                    "dst_ip": dst_ip,
                    "attack_type": attack_type,
                    "severity": "High" if prediction > 1 else "Medium"
                })
            else:
                traffic_stats["normal_packets"] += 1

            # ✅ Add captured packet to traffic_data
            timestamp = int(time.time() * 1000)
            recent_traffic.append({
                "timestamp": timestamp,
                "normal": 1 if prediction == 0 else 0,
                "attack": 1 if prediction > 0 else 0
            })
        except Exception as e:
            print(f"❌ Error in ML Prediction: {e}")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/dashboard-data')
def dashboard_data():
    runtime = time.time() - traffic_stats["start_time"]
    hours, remainder = divmod(runtime, 3600)
    minutes, seconds = divmod(remainder, 60)
    runtime_str = f"{int(hours)}h {int(minutes)}m {int(seconds)}s"
    threat_rate = (traffic_stats["attack_packets"] / traffic_stats["total_packets"] * 100) if traffic_stats["total_packets"] > 0 else 0
    return jsonify({
        "stats": {
            "total_packets": traffic_stats["total_packets"],
            "normal_packets": traffic_stats["normal_packets"],
            "attack_packets": traffic_stats["attack_packets"],
            "threat_rate": f"{threat_rate:.2f}%",
            "runtime": runtime_str
        },
        "alerts": list(alerts),
        "traffic_data": list(recent_traffic)
    })

if __name__ == '__main__':
    monitoring_thread = threading.Thread(target=lambda: sniff(iface="WiFi", prn=live_packet_capture, store=0), daemon=True)
    monitoring_thread.start()
    print("✅ Real-time network monitoring started...")
    app.run(debug=True, host='0.0.0.0', port=5000)
