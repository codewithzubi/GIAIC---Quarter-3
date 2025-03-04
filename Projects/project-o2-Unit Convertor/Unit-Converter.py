import streamlit as st


st.markdown("""
    <style>
    .title {color: #FF5733; text-align: center; font-size: 36px; font-weight: bold;}
    .subtitle {color: #3498DB; text-align: center; font-size: 20px; font-weight: bold;}
    .stButton>button {background-color: #2ECC71; color: white; font-size: 16px;}
    </style>
""", unsafe_allow_html=True)

def length_converter(value, choice):
    if choice == "🔹 Kilometers to Miles":
        return f"🌍 {value} km is **{value * 0.621371} miles** 🚗"
    elif choice == "🔹 Miles to Kilometers":
        return f"🚗 {value} miles is **{value * 1.60934} km** 🌍"

def weight_converter(value, choice):
    if choice == "⚖️ Kilograms to Pounds":
        return f"🏋️ {value} kg is **{value * 2.20462} pounds** 🏋️‍♂️"
    elif choice == "⚖️ Pounds to Kilograms":
        return f"🏋️‍♂️ {value} pounds is **{value * 0.453592} kg** 🏋️"

def temperature_converter(value, choice):
    if choice == "🌡️ Celsius to Fahrenheit":
        return f"🔥 {value}°C is **{(value * 9/5) + 32}°F** ☀️"
    elif choice == "🌡️ Fahrenheit to Celsius":
        return f"❄️ {value}°F is **{(value - 32) * 5/9}°C** 🌡️"

def main():
    st.markdown("<h1 class='title'>✨ Unit Converter ✨</h1>", unsafe_allow_html=True)
   
    option = st.selectbox("🎯 Choose Conversion Type", ["📏 Length Converter", "⚖️ Weight Converter", "🌡️ Temperature Converter"])

    if option == "📏 Length Converter":
        choice = st.radio("🔄 Select Conversion", ["🔹 Kilometers to Miles", "🔹 Miles to Kilometers"])
        value = st.number_input("🔢 Enter Value", min_value=0.0, format="%.2f")
        if st.button("🚀 Convert"):
            st.success(length_converter(value, choice))
    
    elif option == "⚖️ Weight Converter":
        choice = st.radio("🔄 Select Conversion", ["⚖️ Kilograms to Pounds", "⚖️ Pounds to Kilograms"])
        value = st.number_input("🔢 Enter Value", min_value=0.0, format="%.2f")
        if st.button("🚀 Convert"):
            st.success(weight_converter(value, choice))
    
    elif option == "🌡️ Temperature Converter":
        choice = st.radio("🔄 Select Conversion", ["🌡️ Celsius to Fahrenheit", "🌡️ Fahrenheit to Celsius"])
        value = st.number_input("🔢 Enter Value", format="%.2f")
        if st.button("🚀 Convert"):
            st.success(temperature_converter(value, choice))

if __name__ == "__main__":
    main()
