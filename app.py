import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="My Profile",
    page_icon="👤",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f4f6f9;
    }

    .profile-name {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #2c3e50;
    }

    .profile-title {
        text-align: center;
        color: gray;
        font-size: 18px;
    }

    .section-title {
        color: #2c3e50;
        font-size: 23px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to:",
    ["My Profile", "About Me", "My Hobbies"]
)

# ==========================
# MY PROFILE PAGE
# ==========================
if page == "My Profile":

    st.title("MY PERSONAL PROFILE")

    # Profile Picture
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image(
            "images/profile.jpg",
            width=200
        )

    # Name
    st.markdown(
        '<p class="profile-name">Marv Thomas Shalom B. Cuarenta</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="profile-title">Mechanical Engineering Student</p>',
        unsafe_allow_html=True
    )

    st.divider()

    # Personal Information
    st.subheader("Personal Information")

    st.write("👤 **Full Name:** Marv Thomas Shalom B. Cuarenta")
    st.write("🎂 **Age:** 19 years old")
    st.write("📍 **Address:** P-4 Brgy. Maharlika, Surigao del Sur")
    st.write("🎓 **Course:** Bachelor of Science in Mechanical Engineering")
    st.write("🏫 **Year Level:** Second Year College")

    st.divider()

    # Contact Information
    st.subheader("Contact Information")

    st.write("📧 **Email:** marvcuarenta@gmail.com")
    st.write("📱 **Contact Number:** 09317484516")


# ==========================
# ABOUT ME PAGE
# ==========================
elif page == "About Me":

    st.title("ABOUT ME")

    st.write("""
    Hello! My name is Marv Thomas Shalom B. Cuarenta.
    I am 19 years old and currently a second-year
    Mechanical Engineering student.

    I am a dedicated and goal-oriented individual
    who enjoys learning new things, developing my skills,
    and challenging myself to become a better person.

    My goal is to improve my knowledge, gain more
    experience, and become a successful Mechanical Engineer
    in the future.
    """)


# ==========================
# MY HOBBIES PAGE
# ==========================
elif page == "My Hobbies":

    st.title("MY HOBBIES AND INTERESTS")

    st.write("Here are some of my favorite activities:")

    st.write("⚽ Playing sports")
    st.write("🎮 Playing online games")
    st.write("🎵 Listening to MALCOLM TODD")
    st.write("💻 Learning programming")
    st.write("📚 Studying and learning new things")

    st.divider()

    st.subheader("My Goals")

    st.write("""
    - Finish my college degree.
    - Become a successful Mechanical Engineer.
    - Improve my programming skills.
    - Gain more knowledge and experience.
    """)
    
    st.success("Thank you for visiting my My Profile Application!")

st.divider()
st.caption("(c) 2026 Marv Thomas Shalom B. Cuarenta | My Profile Application")
