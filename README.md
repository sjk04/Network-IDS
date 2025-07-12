# 🛡️ IDS.AI – Intelligent Network Intrusion Detection System

**Proactive Protection — Powered by Intelligence**

`IDS.AI` is a machine learning–driven real-time Intrusion Detection System designed to efficiently detect and mitigate DoS and DDoS attacks. Built as a B.Tech Mini Project, this system empowers network security through intelligent traffic analysis and live monitoring.

---

## 🚀 Features

- ✅ **Targeted Detection for DoS/DDoS Attacks**  
  Uses a Random Forest classifier to accurately identify and classify malicious traffic.

- ✅ **Flask-Based Dashboard**  
  A clean web interface for live monitoring, log visualization, and threat trend analysis.

- ✅ **Real-Time Alerts**  
  Instant alerts showing source/destination IP, risk level, and timestamp of the threat.

- ✅ **Threat Classification**  
  Categorizes traffic as *normal* or *malicious* using learned network patterns.

- ✅ **Scalable Monitoring**  
  Efficient packet capture and preprocessing powered by **Scapy**, **Pandas**, and **NumPy**.

---

## 🧠 Machine Learning Model

- **Model Used:** Random Forest Classifier  
- **Dataset:** CICIDS (Canadian Institute for Cybersecurity Intrusion Detection System)  
- **Preprocessing:**  
  - Feature extraction and scaling  
  - Data balancing (DoS/DDoS vs Normal)  
  - Encoding and model persistence via `.pkl` files

> ⚠️ **Note:** Large `.csv` files and datasets are excluded from this repository to keep it lightweight and version-control friendly.  
> You can regenerate them by following the steps in `balance.py` and `scale_features.py` using the CICIDS dataset.

---

## 🛠️ Tech Stack

- **Frontend**: Flask, HTML, CSS  
- **Backend**: Python  
- **ML Libraries**: Scikit-learn, Pandas, NumPy  
- **Network Packet Processing**: Scapy  
- **Data Storage**: Processed `.pkl` files and logs

---

## 📂 Project Structure

network-ids/
│
├── train_model.py # ML model training script
├── test_model.py # Model evaluation
├── balance.py # Dataset balancing script
├── scale_features.py # Feature scaling and processing
├── app.py # Flask web app
│
├── ids_model.pkl # Trained model
├── feature_columns.pkl # Selected features
├── label_encoder.pkl # Label encoder
│
├── static/ # CSS, JS assets
├── templates/ # HTML templates
├── venv/ # Virtual environment (excluded from Git)
└── pycache/ # Python cache files (excluded from Git)

---

## 🧪 How to Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start Flask App
python app.py

# 3. Access Dashboard
Open your browser at http://localhost:5000

👥 Team
Simon J Kurian – ML Model Development & Frontend

Rohan C Anish – Backend & Dataset Handling

Muhammed Fawaz Kalathingal – Data Preprocessing & Integration

Institution: Department of AI & Data Science
Muthoot Institute of Technology and Science, Ernakulam

🎓 Guided by
Ms. Rija Jose
