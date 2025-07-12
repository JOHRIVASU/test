import streamlit as st
import time

# Page config
st.set_page_config(page_title="I'm Sorry, Laya 💖", page_icon="💌", layout="centered")

# Custom styles
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        color: #ff4b4b;
        text-align: center;
        font-weight: bold;
        margin-top: 30px;
    }
    .heart {
        font-size: 50px;
        text-align: center;
        animation: pulse 1s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    .message {
        text-align: center;
        font-size: 22px;
        color: #444;
        padding: 10px 30px;
        line-height: 1.7;
        margin-top: 20px;
    }
    .poem {
        font-size: 20px;
        text-align: center;
        color: #333;
        padding: 20px;
        border-left: 5px solid #ff4b4b;
        background-color: #fff5f5;
        margin-top: 30px;
    }
    .forgive {
        text-align: center;
        margin-top: 40px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">I’m Sorry, Laya 💔</div>', unsafe_allow_html=True)
st.markdown('<div class="heart">❤️</div>', unsafe_allow_html=True)

# Apology message
st.markdown("""
<div class="message">
    <p>Your smile means the world to me.</p>
    <p>Your silence... it’s quietly breaking my heart. 💔</p>

    <p>I’m truly sorry for hurting you, Laya.<br>
    Please forgive me — not just with words, but with your heart.</p>

    <p>Let’s fix this — not stay mad, but grow stronger. 🤝<br>
    Because losing you is something I can't bear.</p>
</div>
""", unsafe_allow_html=True)

# Poem section
st.subheader("A Little Poem Just for You 🌸")

st.markdown("""
<div class="poem">
    In every laugh and every tear,<br>
    You're the one I hold so dear.<br><br>

    Anger fades but love remains,<br>
    Let’s heal hearts and break the chains.<br><br>

    I’m sorry, Laya — please don’t stay mad,<br>
    Without your smile, my world feels sad.
</div>
""", unsafe_allow_html=True)

# Forgive button
st.markdown('<div class="forgive">', unsafe_allow_html=True)
if st.button("🤍 Click here if you forgive me 🤍"):
    st.success("YAY! Thank you Laya! 🥹❤️ You’ve made my day.")
    st.balloons()
st.markdown('</div>', unsafe_allow_html=True)
