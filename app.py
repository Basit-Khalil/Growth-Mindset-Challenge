import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Growth Mindset Challenge",  layout="wide")

# Sidebar for User Details
with st.sidebar:
    st.subheader("👤 User Details")
    name = st.text_input("Enter your name:")
    study = st.selectbox("What is your education level?", ["Matric", "Intermediate", "Undergraduate", "Bachelor", "Graduate"])
    interest = st.selectbox("Select your interest:", ["Technology", "Science", "Arts", "Business", "Health", "Other"])
    goal = st.text_input("What is your Today's growth goal?")
    email = st.text_input("Enter your email (optional):")
    
    if st.button("Save Details"):
        st.success(f"Welcome, {name}! Your details have been saved.")

# App Title
st.title("Growth Mindset Challenge")
st.write("Embrace the power of challenges to grow and develop resilience!")

# Growth Mindset Daily Challenge based on user details
interest_based_challenges = {
    "Technology": ["Learn a new programming concept today.", "Solve a coding challenge.", "Read about an emerging technology."],
    "Science": ["Read a research article in your field.", "Conduct a small experiment.", "Watch a documentary on a scientific breakthrough."],
    "Arts": ["Create a new piece of art.", "Study a famous artist’s work.", "Try a new artistic technique."],
    "Business": ["Read a business case study.", "Analyze a successful entrepreneur’s journey.", "Try a new productivity technique."],
    "Health": ["Do a mindfulness exercise.", "Learn about a new health habit.", "Try a new healthy recipe."],
    "Other": ["Write about a recent challenge you faced.", "Encourage a friend.", "Step out of your comfort zone today."]
}

def get_today_challenge():
    general_challenges = [
        "Reframe a negative thought into a positive one.",
        "Identify a recent challenge and list three things you learned.",
        "Practice gratitude by writing down three things you appreciate today.",
        "Encourage a friend or colleague who is facing difficulties.",
        "Step out of your comfort zone by trying something new today.",
        "Write about a moment where you showed resilience."
    ]
    
    user_interest_challenges = interest_based_challenges.get(interest, [])
    all_challenges = general_challenges + user_interest_challenges
    return random.choice(all_challenges) if all_challenges else "Add a challenge to get started!"

st.subheader("🚀 Today's Challenge")
st.write(get_today_challenge())

# User-Defined Challenges
st.subheader("💡 Add Your Own Challenge")
if "user_challenges" not in st.session_state:
    st.session_state.user_challenges = []

new_challenge = st.text_input("Enter a new challenge to acheive:")
if st.button("Add Challenge"):
    if new_challenge:
        st.session_state.user_challenges.append(new_challenge)
        st.success("Your challenge has been added!")

# Display User Challenges
st.subheader("📌 Your Challenges")
for idx, challenge in enumerate(st.session_state.user_challenges):
    st.write(f"{idx+1}. {challenge}")

# User Reflection Input
st.subheader("📝 Reflection Journal")
reflection = st.text_area("How did you approach today’s challenge? What did you learn?")
if st.button("Save Reflection"):
    st.success("Your reflection has been saved! Keep going!")

# Streak-Based Progress Tracker
st.subheader("🔥 Streak Tracker")
if "streak" not in st.session_state:
    st.session_state.streak = 0

if st.button("Mark Challenge as Completed ✅"):
    st.session_state.streak += 1
    st.success(f"Great job! Your current streak is {st.session_state.streak} days! Keep going!")
