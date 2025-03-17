import streamlit as st # use for UI Design
import pandas as pd  # use for Data manipulation
import datetime # use for handling dates and time
import csv # use for readding and writing csv files
import os # use for file operations

MOOD_FILE = "mode_file.csv"

def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date","Mood"])
    return pd.read_csv(MOOD_FILE)

def save_mood_data(date,mood):
    with open(MOOD_FILE, "a") as file:

        writer = csv.writer(file)
        writer.writerow([date,mood])

st.title("MOOD TRACKER")

today = datetime.date.today()

st.subheader("How are you feeling today...?")

mood = st.selectbox("Select Your Mood",["Happy","Saad","Angry","Neutral"])

if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success("Mood logged successfully!")

data = load_mood_data()

if not data.empty:  
    st.subheader("Mood Trends Over Time")

    data["Date"] = pd.to_datetime(data["Date"])

    mood_countes = data.groupby("Mood").count()["Date"]
    st.bar_chart(mood_countes)







