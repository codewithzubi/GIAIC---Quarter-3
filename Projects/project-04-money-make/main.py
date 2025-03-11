import streamlit as st
import random
import time
import requests

# Set page layout
st.set_page_config(page_title="💸 Money Making Machine", page_icon="💰", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        h1, h2, h3 {
            color: #007BFF;
            text-align: center;
        }
        .stButton>button {
            width: 100%;
            background-color: #28a745;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 10px;
        }
        .stButton>button:hover {
            background-color: #218838;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("💸 Money Making Machine")

# Function to generate random money
def generate_money():
    return random.randint(10, 500)

# Function to fetch side hustles
def fetch_side_hustles():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles.get("side_hustles", ["Freelancing", "Dropshipping"])
        else:
            return ["Freelancing", "Blogging"]
    except:
        return ["Something went wrong! Try again."]

# Function to fetch motivational quotes
def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes.get("money_quotes", ["Money grows when invested wisely!"])
        else:
            return ["Wealth is created, not found."]
    except:
        return ["Something went wrong! Try again."]

# Layout with columns
col1, col2, col3 = st.columns(3)

# Column 1: Money Generator
with col1:
    st.subheader("💰 Instant Cash Generator")
    if st.button("Generate Money"):
        st.write("💵 Counting Your Money...")
        time.sleep(1)
        amount = generate_money()
        st.success(f"🎉 You made **${amount}**!")

# Column 2: Side Hustles Ideas
with col2:
    st.subheader("🚀 Side Hustle Ideas")
    if st.button("Generate Hustles"):
        ideas = fetch_side_hustles()
        st.success("💡 " + (ideas))

# Column 3: Motivational Quotes
with col3:
    st.subheader("🔥 Money Motivation")
    if st.button("Get Inspired"):
        quote = fetch_money_quotes()
        st.info(f"💭 {quote}")
