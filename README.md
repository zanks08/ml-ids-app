# 🚨 AI-Powered Intrusion Detection System (IDS) - Web Application

This project is a **full Machine Learning Intrusion Detection System (IDS)** that predicts whether a network traffic connection is **normal** or an **attack** using the NSL-KDD dataset.  
It is powered by an **XGBoost ML model** and deployed through a **professional Streamlit web app**.


You can **view the live application here**:  
🔗 [View Deployed App](https://ml-ids-app.streamlit.app/)  


---

## 🧠 About This Web Application

The AI IDS app allows users to:

- 📂 **Upload network traffic CSV files**.
- 🤖 **Automatically predict** if each network connection is normal or an attack.
- 📊 **Visualize predictions** through clean graphs (bar chart and pie chart).
- 🚀 **Real-time analysis** with instant results on upload.

Built to simulate **real-world Network Monitoring Tools** for security professionals.

**Main Highlights:**
- XGBoost Model (high-performance, tuned)
- Streamlit Dashboard (beautiful design, responsive layout)
- Drag & Drop CSV Upload Interface
- Professional Data Visualizations (Seaborn + Matplotlib)
- End-to-End Real-time Prediction System

---

## 🛠 How I Built It

1. **Dataset Preparation**  
   - Used the NSL-KDD dataset (KDDTrain+ and KDDTest+).
   - Preprocessed raw traffic data: added headers, handled categorical values, label encoding.

2. **Model Development**
   - Trained an XGBoost Classifier.
   - Performed Hyperparameter tuning (optimized tree depth, learning rate, gamma, regularizations).
   - Achieved ~80% model accuracy on unseen test data.

3. **Web Application Development**
   - Designed a front-end dashboard using **Streamlit**.
   - Integrated trained ML model into the app using **joblib**.
   - Added dynamic file uploaders, real-time data preview, and interactive charts.

4. **Final Testing**
   - Verified app performance with sample CSV uploads.
   - Optimized UI/UX for a clean, modern dashboard experience.

---

## 🚀 How to Run Locally

Follow these simple steps to set up and run the AI IDS app on your machine:

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/ml-ids-app.git
cd ml-ids-app
```

2. Install all dependencies:
```bash
pip install -r requirements.txt
```

3. Run the streamlit web app:
 ```bash
streamlit run app.py
```

---

## 📊 Dataset Information

- **Dataset:** NSL-KDD (an improved version of KDD Cup 1999)
- **Source:**  
  [NSL-KDD Dataset Source](https://www.unb.ca/cic/datasets/nsl.html)

**Features Include:**
- Duration, protocol type, service, flag
- Number of failed logins, compromised conditions
- Various connection statistics (bytes sent, errors, rates)

The **target variable** indicates whether the connection was an **attack** or **normal**.

---

## 📌 Technologies Used

| Tool | Purpose |
|------|---------|
| Python | Programming Language |
| XGBoost | Machine Learning Model |
| Scikit-Learn | Preprocessing and Metrics |
| Pandas | Data Handling |
| Streamlit | Web App Deployment |
| Seaborn/Matplotlib | Data Visualization |

---

## 🔗 References

- [NSL-KDD Dataset Source](https://www.unb.ca/cic/datasets/nsl.html)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Original KDD Cup 1999 Dataset](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)

---


Built with ❤️ by **Harshitha Sha** 🚀  

