import streamlit as st
import pandas as pd
from analyzer import analyze_packet
from detector import detect_anomaly

st.title("🚀 Network Traffic Analyzer")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    results = []

    for _, row in df.iterrows():
        data = analyze_packet(row)

        if data:
            alerts = detect_anomaly(data)
            data['alerts'] = alerts
            results.append(data)

    st.success("Analysis Completed ✅")
    st.dataframe(results)