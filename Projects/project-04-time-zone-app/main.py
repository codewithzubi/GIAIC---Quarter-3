import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo



TIME_ZONE = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Asia/Tokyo",
    "Europe/Landon",
    "Europe/Paris",
    "Australia/Sydeny"
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata"
    "Asia/Bangkok",
    "Australia/Melbourne",
    "Asia/Shanghai",
    "Europe/London",
    "America/Los_Angeles",
]

st.title("TIME ZONE APP")

selected_time_zone = st.multiselect("Select Timezone",TIME_ZONE,default=["UTC","Asia/Karachi"])
st.subheader("Selected Timezones")
for tz in selected_time_zone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
    st.write(f"**{tz}**: {current_time}")

st.subheader("Convert Time Between Timezone")
current_time = st.time_input("Current Time",value=datetime.now().time())
from_tz = st.selectbox("Form Timezone", TIME_ZONE, index=0)
to_tz = st.selectbox("To Timezone", TIME_ZONE, index=1)
if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(),current_time,tzinfo=ZoneInfo(from_tz))

    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")
    st.success(f"Converted Time in {to_tz}: {converted_time}")

