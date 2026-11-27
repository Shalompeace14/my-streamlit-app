import streamlit as st

st.set_page_config(page_title="Marv | Personal Profile", page_icon="💙", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.stApp { background: linear-gradient(145deg, #f2f8ff, #e7f1ff 55%, #f8fbff); color: #102a56; }
[data-testid="stHeader"] { background: transparent; }
[data-testid="stSidebar"] { background: linear-gradient(180deg, #0d63d9, #123b83); }
[data-testid="stSidebar"] * { color: white; }
[data-testid="stSidebar"] [role="radiogroup"] label { border-radius: 12px; padding: 8px 10px; transition: .2s; }
[data-testid="stSidebar"] [role="radiogroup"] label:hover { background: rgba(255,255,255,.15); transform: translateX(4px); }
h1, h2, h3 { color: #102a56; }
.hero { text-align: center; animation: rise .7s ease both; }
.hero-badge { display:inline-block; padding:7px 14px; color:#0756c9; background:#dcecff; border:1px solid #bdd6fa; border-radius:999px; font-size:13px; font-weight:700; }
.profile-name { text-align:center; margin:14px 0 2px; color:#102a56; font-size:clamp(26px,5vw,36px); font-weight:800; }
.profile-title { text-align:center; color:#647a9c; font-size:17px; }
.blue-card { background:rgba(255,255,255,.82); border:1px solid rgba(94,159,255,.22); border-radius:20px; padding:20px; box-shadow:0 12px 35px rgba(27,91,170,.09); transition:.22s; margin:10px 0; }
.blue-card:hover { transform:translateY(-4px); box-shadow:0 18px 42px rgba(27,91,170,.16); }
.bubble { width:fit-content; max-width:88%; padding:12px 16px; margin:8px 0; border-radius:18px 18px 18px 5px; background:#edf5ff; border:1px solid #d5e8ff; color:#173c70; box-shadow:0 5px 15px rgba(22,91,170,.07); }
.bubble-user { margin-left:auto; border-radius:18px 18px 5px 18px; background:linear-gradient(135deg,#2583ff,#1765db); border:0; color:white; }
.stButton>button { border:0; border-radius:12px; color:white; background:linear-gradient(110deg,#2583ff,#0756c9); font-weight:700; box-shadow:0 6px 16px rgba(37,131,255,.22); transition:.2s; }
.stButton>button:hover { transform:translateY(-2px); box-shadow:0 10px 22px rgba(37,131,255,.32); color:white; }
@keyframes rise { from {opacity:0; transform:translateY(12px)} to {opacity:1; transform:translateY(0)} }
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## 💙 Marv's Space")
st.sidebar.caption("A little corner of my world")
page = st.sidebar.radio("Explore", ["👤 My Profile", "✨ About Me", "🎯 Hobbies & Goals", "💬 Bubble Chat"], label_visibility="collapsed")
st.sidebar.markdown("---")
st.sidebar.markdown("🫧 *Choose a page and explore!*")

if page == "👤 My Profile":
    st.markdown('<div class="hero"><span class="hero-badge">💙 WELCOME TO MY PROFILE</span></div>', unsafe_allow_html=True)
    left, center, right = st.columns([1, 1.2, 1])
    with center:
        st.image("images/profile.jpg", width=200)
    st.markdown('<div class="profile-name">Marv Thomas Shalom B. Cuarenta</div>', unsafe_allow_html=True)
    st.markdown('<div class="profile-title">⚙️ Mechanical Engineering Student</div>', unsafe_allow_html=True)

    st.markdown('<div class="blue-card">', unsafe_allow_html=True)
    st.subheader("🪪 Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        st.write("👤 **Full Name**\n\nMarv Thomas Shalom B. Cuarenta")
        st.write("🎂 **Age**\n\n19 years old")
        st.write("📍 **Address**\n\nP-4 Brgy. Maharlika, Surigao del Sur")
    with col2:
        st.write("🎓 **Course**\n\nBachelor of Science in Mechanical Engineering")
        st.write("🏫 **Year Level**\n\nSecond Year College")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="blue-card">', unsafe_allow_html=True)
    st.subheader("📬 Contact Information")
    st.write("📧 **Email:** marvcuarenta@gmail.com")
    st.write("📱 **Contact Number:** 09317484516")
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "✨ About Me":
    st.title("✨ A little about me")
    st.markdown('<div class="blue-card">', unsafe_allow_html=True)
    st.write("Hello! My name is Marv Thomas Shalom B. Cuarenta. I'm 19 years old and currently a second-year Mechanical Engineering student.")
    st.write("I'm a dedicated and goal-oriented person who enjoys learning new things, developing my skills, and challenging myself to become better.")
    st.info("🚀 My goal is to keep growing, gain experience, and become a successful Mechanical Engineer.")
    st.markdown('</div>', unsafe_allow_html=True)

    focus = st.selectbox("What would you like to know more about?", ["Choose a topic...", "My studies", "My goals", "My personality"])
    details = {"My studies": "I'm studying Mechanical Engineering and enjoy learning how things work.", "My goals": "I want to finish college, build my skills, and become a successful engineer.", "My personality": "I'm dedicated, goal-oriented, and always open to learning something new."}
    if focus in details:
        st.markdown(f'<div class="bubble">💬 {details[focus]}</div>', unsafe_allow_html=True)

elif page == "🎯 Hobbies & Goals":
    st.title("🎯 Hobbies & interests")
    st.caption("A few things I enjoy doing in my free time:")
    hobbies = ["⚽ Playing sports", "🎮 Playing online games", "🎵 Listening to MALCOLM TODD", "💻 Learning programming", "📚 Studying and learning new things"]
    cols = st.columns(2)
    for index, hobby in enumerate(hobbies):
        with cols[index % 2]:
            st.markdown(f'<div class="blue-card">{hobby}</div>', unsafe_allow_html=True)

    st.subheader("🚀 My Goals")
    for goal in ["Finish my college degree", "Become a successful Mechanical Engineer", "Improve my programming skills", "Gain more knowledge and experience"]:
        st.checkbox(goal, key=f"goal_{goal}")
    st.caption("Tick a goal to celebrate the steps you're working toward.")

elif page == "💬 Bubble Chat":
    st.title("💬 Bubble Chat")
    st.caption("Say hello! This chat uses a few friendly, built-in replies.")

    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [{"role":"assistant", "content":"Hi there! 👋 Welcome to my profile. Ask me about my studies, hobbies, or goals!"}]

    for message in st.session_state.chat_messages:
        bubble_class = "bubble-user" if message["role"] == "user" else ""
        icon = "🧑‍💻" if message["role"] == "user" else "💙"
        st.markdown(f'<div class="bubble {bubble_class}">{icon} {message["content"]}</div>', unsafe_allow_html=True)

    prompt = st.chat_input("Type a message...")
    if prompt:
        st.session_state.chat_messages.append({"role":"user", "content":prompt})
        question = prompt.lower()
        if any(word in question for word in ["study", "course", "school", "engineering"]):
            reply = "I'm a second-year Mechanical Engineering student. ⚙️"
        elif any(word in question for word in ["hobby", "hobbies", "like", "music", "game"]):
            reply = "I enjoy sports, online games, listening to MALCOLM TODD, and learning programming. 🎵"
        elif any(word in question for word in ["goal", "future", "dream"]):
            reply = "My goal is to finish college and become a successful Mechanical Engineer. 🚀"
        elif any(word in question for word in ["hello", "hi", "hey"]):
            reply = "Hey! 😊 Thanks for stopping by. What would you like to know?"
        else:
            reply = "Thanks for your message! Try asking about my studies, hobbies, or goals. 💙"
        st.session_state.chat_messages.append({"role":"assistant", "content":reply})
        st.rerun()

    if st.button("🧹 Clear chat"):
        st.session_state.chat_messages = []
        st.rerun()

st.divider()
st.caption("💙 © 2026 Marv Thomas Shalom B. Cuarenta | My Profile Application")
