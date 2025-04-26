import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Load trained model
model = joblib.load("model/ids_model.pkl")

# Set Streamlit page config
st.set_page_config(page_title="Intrusion Detection System (IDS)", layout="wide")

# Sidebar About Section
with st.sidebar:
    st.title("About This App")
    st.success("🚀 Created by **Harshitha** 🌟\n\nMachine Learning Based Intrusion Detection System.\n\nUpload network traffic data and detect if it's Normal or an Attack in real-time.")

# Main Title
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🚨 AI Intrusion Detection System (IDS)</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: gray;'>Upload network traffic data and let AI predict attacks automatically</h5>", unsafe_allow_html=True)
st.markdown("---")

# File Upload
st.subheader("📂 Upload your CSV file")
uploaded_file = st.file_uploader("Choose a CSV file (Limit: 200MB)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.markdown("### 🔍 Uploaded Data Preview:")
    st.dataframe(df, use_container_width=True)

    # Predict
    predictions = model.predict(df)

    # Map 0/1 to text
    pred_labels = ["attack" if pred == 0 else "normal" for pred in predictions]
    prediction_df = pd.DataFrame(pred_labels, columns=["Prediction"])

    st.markdown("### 📈 Predictions Summary:")
    st.dataframe(prediction_df, use_container_width=True)

    # Visualization
    st.markdown("### 📊 Visualization:")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Attack vs Normal Distribution")
        plt.figure(figsize=(6, 4))
        sns.countplot(x=prediction_df["Prediction"], palette="Set2")
        plt.title("Prediction Count")
        plt.xlabel("Prediction")
        plt.ylabel("Count")
        st.pyplot(plt.gcf())

    with col2:
        st.markdown("#### Attack vs Normal Pie Chart")
        pie_data = prediction_df["Prediction"].value_counts()
        fig, ax = plt.subplots()
        ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2'))
        ax.axis('equal')
        st.pyplot(fig)

else:
    st.info("Please upload a CSV file to get started!")

# Footer
st.markdown("---")
st.markdown("<h6 style='text-align: center; color: gray;'>Built with ❤️ by Harshitha</h6>", unsafe_allow_html=True)
