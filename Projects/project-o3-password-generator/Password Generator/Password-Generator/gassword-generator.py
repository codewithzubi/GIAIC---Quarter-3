import streamlit as st
import random
import string

# Function to generate a password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    
    if use_special:
        characters += string.punctuation
    
    return ''.join(random.choice(characters) for _ in range(length))

# Custom CSS for dark theme with white text
st.markdown("""
    <style>
       
        .stApp {
            background: #1d1d1d;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4);
        }
        h1 {
            color: #ffffff;  /* Set heading color to white */
            font-size: 3em;
            text-align: center;
            font-weight: 700;
            margin-bottom: 0.5em;
        }
        .stButton>button {
            background-color: #00e676 !important;
            color: white !important;  /* Ensures button text is white */
            border-radius: 12px;
            font-size: 18px;
            padding: 16px;
            width: 100%;
            border: none;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            transition: background-color 0.3s, transform 0.3s;
        }
        .stButton>button:hover {
            background-color: #76ff03 !important;
            transform: translateY(-3px);
        }
        .stSlider>div, .stSlider label {
            color: #ffffff !important;
            font-size: 16px;
            font-weight: bold !important;
        }
        .stCheckbox label {
            color: #ffffff !important;
            font-weight: bold !important;
            font-size: 16px;
        }
        .stCheckbox>div {
            background-color: #333333 !important;
            border-radius: 5px;
        }
        .stCheckbox input[type="checkbox"]:checked {
            background-color: #00e676 !important;
        }
        .stCheckbox input[type="checkbox"]:not(:checked) {
            background-color: #616161 !important;
        }
        .stTextInput input {
            background-color: #333333 !important;
            color: #ffffff !important;  /* Ensures input text is white */
            border: 2px solid #616161;
            border-radius: 8px;
            padding: 12px;
            font-size: 16px;
            transition: all 0.3s ease;
        }
        .stTextInput input:focus {
            border-color: #00e676 !important;
            outline: none;
        }
        .stSuccess {
            color: #76ff03 !important;
            font-weight: bold;
            font-size: 18px;
        }
        hr {
            border: 1px solid #00e676;
        }
        a {
            color: #00e676 !important;
            text-decoration: none;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<h1>🔐 Secure Password Generator</h1>", unsafe_allow_html=True)

# User Inputs
length = st.slider("🔢 Select Password Length", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("🔢 Include Digits")
use_special = st.checkbox("✨ Include Special Characters")

# Generate Password Button
if st.button("🔑 Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"✅ Generated Password: `{password}`")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made with ❤️ by <a href='https://github.com/codewithzubi' target='_blank'>Zubair Ahmed</a></p>", unsafe_allow_html=True)
