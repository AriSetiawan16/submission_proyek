import streamlit as st
import pandas as pd

# Load dataset
file_path = "submission_ari.csv"
df = pd.read_csv(file_path)

# Page Configurations
st.set_page_config(page_title="Air Quality Dashboard", layout="wide", initial_sidebar_state="expanded")

# Sidebar Menu
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1163/1163624.png", width=100)
st.sidebar.title("🌍 Air Quality Dashboard")
st.sidebar.markdown("---")
st.sidebar.header("🔍 Filter Data")
station_choice = st.sidebar.selectbox("Pilih Stasiun", df['station'].unique())
df_filtered = df[df['station'] == station_choice]

# Main Content
st.title("🌍 Air Quality Dashboard")
st.markdown("### Analisis Kualitas Udara berdasarkan Dataset")
st.markdown("---")

st.subheader("📊 Distribusi Polutan")
df_air_quality = df[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].dropna()
st.bar_chart(df_air_quality)

st.markdown("---")
st.subheader("📈 Tren PM2.5 per Bulan")
df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
df_monthly = df.groupby(['year', 'month'])['PM2.5'].mean().reset_index()
df_monthly['time'] = pd.to_datetime(df_monthly[['year', 'month']].assign(day=1))
st.line_chart(df_monthly.set_index('time')['PM2.5'])

st.markdown("---")
st.subheader("🔗 Hubungan antara PM2.5 dan Variabel Cuaca")
selected_features = ['PM2.5', 'TEMP', 'PRES', 'DEWP']
df_pairplot = df[selected_features].dropna()
st.scatter_chart(df_pairplot)

# Set background color
st.markdown(
    """
    <style>
        body {
            background-color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)
