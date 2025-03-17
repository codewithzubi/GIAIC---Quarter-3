import streamlit as st  # UI Design
import pandas as pd  # Data manipulation
import datetime  # Handling dates and time
import csv  # Reading and writing CSV files
import os  # File operations

# File to store mood data
MOOD_FILE = "mode_file.csv"

# Function to load existing mood data
def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(MOOD_FILE)

# Function to save mood data
def save_mood_data(date, mood):
    with open(MOOD_FILE, "a") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

# Apply custom UI styling
st.set_page_config(page_title="Mood Tracker", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f4;
    }
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #4CAF50;
    }
    .subheader {
        font-size: 20px;
        font-weight: bold;
        color: #333;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        border-radius: 10px;
        border: none;
        font-size: 16px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="title">🌈 MOOD TRACKER</p>', unsafe_allow_html=True)

today = datetime.date.today()

st.markdown('<p class="subheader">How are you feeling today? 🤔</p>', unsafe_allow_html=True)

# Mood selection with emojis
mood_options = {
    "😀 Happy": "Happy",
    "😢 Sad": "Sad",
    "😡 Angry": "Angry",
    "😐 Neutral": "Neutral"
}

mood = st.selectbox("Select Your Mood", list(mood_options.keys()))

if st.button("Log Mood"):
    save_mood_data(today, mood_options[mood])
    st.success("✅ Mood logged successfully!")

# Load and display mood data
data = load_mood_data()

if not data.empty:
    st.markdown('<p class="subheader">📊 Mood Trends Over Time</p>', unsafe_allow_html=True)

    data["Date"] = pd.to_datetime(data["Date"])
    mood_counts = data.groupby("Mood").count()["Date"]
    
    # Display bar chart with better visualization
    st.bar_chart(mood_counts)
