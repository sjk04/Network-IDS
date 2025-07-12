# 🛡️ IDS.AI – Intelligent Network Intrusion Detection System

**Proactive Protection — Powered by Intelligence**

`IDS.AI` is a machine learning–driven real-time Intrusion Detection System designed to efficiently detect and mitigate DoS and DDoS attacks. Built as a B.Tech Mini Project, this system aims to empower network security through intelligent traffic analysis and live monitoring.

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

---

## 🛠️ Tech Stack

- **Frontend**: Flask, HTML, CSS  
- **Backend**: Python  
- **ML Libraries**: Scikit-learn, Pandas, NumPy  
- **Network Packet Processing**: Scapy  
- **Data Storage**: CSV logs for attack data and real-time monitoring

---

## 📁 Dataset Access

> 🚫 **Note:**  
> The original dataset files (e.g., `balanced_dataset.csv`, `scaled_dataset.csv`) have been **intentionally removed** from the repository to reduce its size and clean commit history.  
>
> 📁 Please place the required `.csv` files inside the `Datasets/` folder **manually** before running training or evaluation scripts.  
>
> 📥 You may retrieve the datasets from:
> - Your local copy
> - An institutional shared drive (if applicable)
> - Public sources like [CICIDS Dataset](https://www.unb.ca/cic/datasets/ids.html)

---

## 📂 Project Structure

```bash
network-ids/
│
├── train_model.py               # ML model training script
├── test_model.py                # Model evaluation
├── balance.py                   # Dataset balancing script
├── scale_features.py            # Feature scaling and processing
├── app.py                       # Flask web app
│
├── ids_model.pkl                # Trained model
├── feature_columns.pkl          # Selected features
├── label_encoder.pkl            # Label encoder
│
├── static/                      # CSS, JS assets
├── templates/                   # HTML templates
├── Datasets/                    # Folder for dataset CSV files (excluded from Git)
├── requirements.txt             # Python dependencies
└── README.md
How to Run
# 1. Install dependencies
pip install -r requirements.txt

# 2. Place required CSV files into the Datasets/ folder

# 3. Start Flask App
python app.py

# 4. Access the Dashboard
Visit http://localhost:5000 in your browser
👥 Team
Simon J Kurian – ML Model Development & Frontend

Rohan C Anish – Backend & Dataset Handling

Muhammed Fawaz Kalathingal – Data Preprocessing & Integration

Institution:
Department of AI & Data Science
Muthoot Institute of Technology and Science, Ernakulam

🎓 Guided by
Ms. Rija Jose
Assistant Professor
Dept. of AI & Data Science

