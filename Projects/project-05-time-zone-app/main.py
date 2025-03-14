import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# Define available time zones correctly
TIME_ZONES = [
    "UTC", "Asia/Karachi", "America/New_York", "Asia/Tokyo",
    "Europe/London", "Europe/Paris", "Australia/Sydney",
    "Europe/Berlin", "Asia/Dubai", "Asia/Kolkata",
    "Asia/Bangkok", "Australia/Melbourne", "Asia/Shanghai",
    "America/Los_Angeles"
]

# Page title with styling
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🕒 Time Zone Converter 🌍</h1>", unsafe_allow_html=True)
st.markdown("---")

# Select multiple time zones for current time display
st.subheader("🌎 Current Time in Selected Timezones")
selected_time_zones = st.multiselect(
    "Select Timezones:",
    TIME_ZONES,
    default=["UTC", "Asia/Karachi"]
)

# Display current time for selected time zones
st.markdown("### ⏳ Live Time Updates:")
for tz in selected_time_zones:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d | %I:%M:%S %p")
    st.markdown(f"<p style='font-size: 18px; color: #2196F3;'><b>{tz}</b>: {current_time}</p>", unsafe_allow_html=True)

st.markdown("---")

# Time conversion section
st.subheader("🔄 Convert Time Between Timezones")
current_time = st.time_input("Select Time:", value=datetime.now().time())
from_tz = st.selectbox("🌍 From Timezone:", TIME_ZONES, index=0)
to_tz = st.selectbox("🌍 To Timezone:", TIME_ZONES, index=1)

if st.button("🔄 Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d | %I:%M:%S %p")

    st.success(f"✅ Converted Time in **{to_tz}**: {converted_time}")

# Footer with Zubair's GitHub profile
st.markdown("---")
st.markdown("""
<p style='text-align: center; font-size: 14px; color: gray;'>
    Built with ❤️ by <a href='https://github.com/codewithzubi' target='_blank' style='color: #2196F3; text-decoration: none; font-weight: bold;'>Zubair Ahmed</a> using Python & Streamlit
</p>
""", unsafe_allow_html=True)
