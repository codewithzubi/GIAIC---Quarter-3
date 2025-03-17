import streamlit as st
import random
import time

# App Title with Emoji
st.title("📝 QUIZ APP")
st.markdown("### Test your knowledge with this fun quiz! 🎯")

# Custom Styling
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        font-size: 18px;
        border-radius: 8px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stRadio div {
        font-size: 16px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Questions Data
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "option": ["Karachi", "Lahore", "Islamabad", "Hyderabad"],
        "answer": "Islamabad"
    },
    {
        "question": "Which language is primarily spoken in Brazil?",
        "option": ["Spanish", "Portuguese", "French", "English"],
        "answer": "Portuguese"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "option": ["Ag", "Au", "Pb", "Fe"],
        "answer": "Au"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "option": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "option": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "option": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Which animal is known as the 'King of the Jungle'?",
        "option": ["Tiger", "Elephant", "Lion", "Cheetah"],
        "answer": "Lion"
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "option": ["90°C", "100°C", "110°C", "120°C"],
        "answer": "100°C"
    },
    {
        "question": "Which is the longest river in the world?",
        "option": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
        "answer": "Nile River"
    },
    {
        "question": "Which continent is the Sahara Desert located in?",
        "option": ["Asia", "Africa", "Australia", "South America"],
        "answer": "Africa"
    }
]

# Session State for Question Handling
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)
    st.session_state.score = 0
    st.session_state.total_attempts = 0

question = st.session_state.current_question

# Progress Bar
progress = min(st.session_state.total_attempts / len(questions), 1.0)
st.progress(progress)


# Display Question
st.markdown(f"### ❓ {question['question']}")

# Radio Button for Options
selected_option = st.radio("Choose Your Answer", question["option"], key="answer")

# Submit Button
if st.button("✅ Submit Answer"):
    st.session_state.total_attempts += 1
    if selected_option == question["answer"]:
        st.success("🎉 Correct Answer! Well done! ✅")
        st.balloons()
        st.session_state.score += 1
    else:
        st.error(f"❌ Incorrect Answer! The Correct Answer is **{question['answer']}**")

    # Wait for 2 seconds and load new question
    time.sleep(2)
    st.session_state.current_question = random.choice(questions)
    st.rerun()

# Show Score
st.sidebar.markdown(f"### 🎯 Score: {st.session_state.score} / {st.session_state.total_attempts}")
