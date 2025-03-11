import streamlit as st
import random
import time
import requests



st.title("Money Making Machine")

def grenrate_money():
    return random.randint(1, 100)
st.subheader("Instant Cash Generator")
if st.button(" Generate Money"):
    st.write("Counting Your Money...")
    time.sleep(1)
    amount = grenrate_money()
    st.success(f"You made ${amount}!")

def fetch_side_hustles():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = reponse.json()
            return hustles["side_hustles"]
        else:
            return ("Freelancing")
    except:
        return ("Somthing want wrong!!")
st.subheader("Side Hustles Ideas")
if st.button("Generate Hustles"):
    idea = fetch_side_hustles()
    st.success(idea)

def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quotes"]
        else:
            return ("Money is the root of all evil!!")
    except:
        return ("Somthing want wrong!!")
st.subheader("Money-Making Motivation")
if st.button("Get Inspired"):
    idea = fetch_money_quotes()
    st.info(idea)