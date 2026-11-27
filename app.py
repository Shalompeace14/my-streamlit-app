import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Marv | Personal Profile", page_icon="💙", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700;800&display=swap');
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.stApp { background: linear-gradient(-45deg, #e9f4ff, #dcecff, #f4faff, #d5e8ff); background-size: 350% 350%; animation: ocean-shift 18s ease infinite; color: #102a56; }
[data-testid="stHeader"] { background: transparent; }
[data-testid="stSidebar"] { background: linear-gradient(180deg, #0d63d9, #123b83); }
[data-testid="stSidebar"] * { color: white; }
h1, h2, h3 { color: #102a56; }
.hero { text-align: center; }
.hero-badge { display: inline-block; padding: 7px 14px; color: #0756c9; background: #dcecff; border: 1px solid #bdd6fa; border-radius: 999px; font-size: 13px; font-weight: 700; }
.profile-name { text-align: center; margin: 14px 0 2px; color: #102a56; font-size: clamp(26px, 5vw, 36px); font-weight: 800; }
.profile-title { text-align: center; color: #647a9c; font-size: 17px; }
.blue-card { background: rgba(255,255,255,.84); border: 1px solid rgba(94,159,255,.24); border-radius: 20px; padding: 20px; box-shadow: 0 12px 35px rgba(27,91,170,.10); margin: 10px 0; }
.profile-photo img { border-radius: 50%; border: 5px solid white; box-shadow: 0 10px 35px rgba(31,106,210,.25); }
/* Descriptions use clean rectangular panels instead of speech bubbles. */
.description-bubble { box-sizing: border-box; width: 100%; max-width: 100%; padding: 12px 16px; margin: 8px 0; border-radius: 8px; background: linear-gradient(110deg, rgba(220,236,255,.78), rgba(237,245,255,.92)); border: 1px solid rgba(94,159,255,.28); border-left: 4px solid #2583ff; color: #173c70; box-shadow: 0 3px 10px rgba(27,91,170,.07); transition: transform .16s ease, background .16s ease, box-shadow .16s ease, color .16s ease; cursor: pointer; }
.description-bubble:hover { background: linear-gradient(110deg, #d4e8ff, #eaf4ff); box-shadow: 0 6px 16px rgba(37,131,255,.16); transform: translateY(-2px); }
.description-bubble:active { background: linear-gradient(110deg, #2583ff, #0756c9); border-color: #0756c9; color: white; box-shadow: 0 2px 6px rgba(7,86,201,.24); transform: scale(.98); }
.description-bubble.full-width { width: 100%; max-width: 100%; }
.bubble { width: fit-content; max-width: 88%; padding: 12px 16px; margin: 8px 0; border-radius: 18px 18px 18px 5px; background: linear-gradient(135deg,#edf5ff,#dcecff); border: 1px solid #bdd6fa; color: #173c70; box-shadow: 0 6px 16px rgba(37,131,255,.12); }
.bubble-user { margin-left: auto; border-radius: 18px 18px 5px 18px; background: linear-gradient(135deg,#2583ff,#1765db); border: 0; color: white; }
.stButton>button { border: 0; border-radius: 12px; color: white; background: linear-gradient(110deg,#2583ff,#0756c9); font-weight: 700; }
.blue-card [data-testid="stMarkdownContainer"] p { margin-bottom: 0; }
@keyframes ocean-shift { 0% {background-position:0% 50%} 50% {background-position:100% 50%} 100% {background-position:0% 50%} }
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation-duration:.01ms !important; transition-duration:.01ms !important; } }
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## 💙 Marv's Space")
st.sidebar.caption("A little corner of my world")
page = st.sidebar.radio("Explore", ["👤 My Profile", "✨ About Me", "🎯 Hobbies & Goals", "💬 Bubble Chat"], label_visibility="collapsed")
st.sidebar.markdown("---")
st.sidebar.markdown("🫧 *Choose a page and explore!*")

if page == "👤 My Profile":
    st.markdown('<div class="hero"><span class="hero-badge">💙 WELCOME TO MY PROFILE</span><h1>Get to know me!</h1><p>Engineering student • Curious mind • Always learning</p></div>', unsafe_allow_html=True)
    _, center, _ = st.columns([1, 1.2, 1])
    with center:
        st.markdown('<div class="profile-photo">', unsafe_allow_html=True)
        st.image("shalom.jpg", width=200)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="profile-name">Marv Thomas Shalom B. Cuarenta</div>', unsafe_allow_html=True)
    st.markdown('<div class="profile-title">⚙️ Mechanical Engineering Student</div>', unsafe_allow_html=True)

    st.markdown('<div class="blue-card">', unsafe_allow_html=True)
    st.subheader("🪪 A little about me")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="description-bubble full-width"><b>👤 Full Name</b><br>Marv Thomas Shalom B. Cuarenta</div>', unsafe_allow_html=True)
        st.markdown('<div class="description-bubble full-width"><b>🎂 Age</b><br>19 years old</div>', unsafe_allow_html=True)
        st.markdown('<div class="description-bubble full-width"><b>📍 Address</b><br>P-4 Brgy. Maharlika, Surigao del Sur</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="description-bubble full-width"><b>🎓 Course</b><br>Bachelor of Science in Mechanical Engineering</div>', unsafe_allow_html=True)
        st.markdown('<div class="description-bubble full-width"><b>🏫 Year Level</b><br>Second Year College</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="blue-card">', unsafe_allow_html=True)
    st.subheader("📬 Contact Information")
    st.markdown('<div class="description-bubble"><b>📧 Email</b> marvcuarenta@gmail.com</div>', unsafe_allow_html=True)
    st.markdown('<div class="description-bubble"><b>📱 Contact Number</b> 09317484516</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="blue-card">', unsafe_allow_html=True)
    st.subheader("🎵 Currently on repeat")
    st.markdown('<div class="description-bubble"><b>“I Just Got Mad” — Malcolm Todd</b></div>', unsafe_allow_html=True)
    st.markdown('<div class="description-bubble"><b>🎧</b> Play the track below. Spotify may ask you to sign in or open the Spotify app.</div>', unsafe_allow_html=True)
    components.html('<iframe style="border-radius:14px" src="https://open.spotify.com/embed/track/5cEbOJ1W1cgWJ3LGeRBsn7?utm_source=generator" width="100%" height="152" frameborder="0" allowfullscreen></iframe>', height=160)
    st.markdown('<div class="description-bubble">[Open on Spotify](https://open.spotify.com/track/5cEbOJ1W1cgWJ3LGeRBsn7) · [Open on Apple Music](https://music.apple.com/us/album/i-just-got-mad-single/1747650424)</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "✨ About Me":
    st.title("✨ A little about me")
    st.markdown('<div class="blue-card">', unsafe_allow_html=True)
    st.markdown('<div class="description-bubble">Hello! My name is Marv Thomas Shalom B. Cuarenta. I’m 19 years old and currently a second-year Mechanical Engineering student.</div>', unsafe_allow_html=True)
    st.markdown('<div class="description-bubble">I’m a dedicated and goal-oriented person who enjoys learning new things, developing my skills, and challenging myself to become better.</div>', unsafe_allow_html=True)
    st.markdown('<div class="description-bubble"><b>🚀 My goal:</b> Keep growing, gain experience, and become a successful Mechanical Engineer.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    focus = st.selectbox("What would you like to know more about?", ["Choose a topic...", "My studies", "My goals", "My personality"])
    details = {"My studies": "I'm studying Mechanical Engineering and enjoy learning how things work.", "My goals": "I want to finish college, build my skills, and become a successful engineer.", "My personality": "I'm dedicated, goal-oriented, curious, and always willing to learn."}
    if focus in details:
        st.markdown(f'<div class="bubble">💬 {details[focus]}</div>', unsafe_allow_html=True)

elif page == "🎯 Hobbies & Goals":
    st.title("🎯 Hobbies & interests")
    st.markdown('<div class="description-bubble">A few things I enjoy doing in my free time:</div>', unsafe_allow_html=True)
    hobbies = ["⚽ Playing sports", "🎮 Playing online games", "🎵 Listening to MALCOLM TODD", "💻 Learning programming", "📚 Studying and learning new things"]
    cols = st.columns(2)
    for index, hobby in enumerate(hobbies):
        with cols[index % 2]:
            st.markdown(f'<div class="description-bubble">{hobby}</div>', unsafe_allow_html=True)
    st.subheader("🚀 My Goals")
    for goal in ["Finish my college degree", "Become a successful Mechanical Engineer", "Improve my programming skills", "Gain more knowledge and experience"]:
        st.checkbox(goal, key=f"goal_{goal}")
    st.markdown('<div class="description-bubble">Tick a goal to celebrate the steps you’re working toward.</div>', unsafe_allow_html=True)

elif page == "💬 Bubble Chat":
    st.title("💬 Bubble Chat")
    st.markdown('<div class="description-bubble">Say hello! This chat uses a few friendly, built-in replies.</div>', unsafe_allow_html=True)
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [{"role": "assistant", "content": "Hi there! 👋 Welcome to my profile. Ask me about my studies, hobbies, or goals!"}]
    for message in st.session_state.chat_messages:
        bubble_class = "bubble-user" if message["role"] == "user" else ""
        icon = "🧑‍💻" if message["role"] == "user" else "💙"
        st.markdown(f'<div class="bubble {bubble_class}">{icon} {message["content"]}</div>', unsafe_allow_html=True)
    prompt = st.chat_input("Type a message...")
    if prompt:
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
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
        st.session_state.chat_messages.append({"role": "assistant", "content": reply})
        st.rerun()
    if st.button("🧹 Clear chat"):
        st.session_state.chat_messages = []
        st.rerun()

st.divider()
st.markdown('<div class="description-bubble full-width">💙 © 2026 Marv Thomas Shalom B. Cuarenta | My Profile Application</div>', unsafe_allow_html=True)
