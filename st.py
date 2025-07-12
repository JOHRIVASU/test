import streamlit as st
import time

st.set_page_config(page_title="Sorry Laya 💔", page_icon="💌", layout="centered")

# Styling
st.markdown("""
    <style>
    .title { font-size: 40px; color: #ff4b4b; text-align: center; font-weight: bold; }
    .subtitle { font-size: 24px; color: #333333; text-align: center; }
    .heart { font-size: 50px; text-align: center; animation: pulse 1s infinite; }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    .forgive { text-align: center; margin-top: 40px; }
    </style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<div class="title">I’m Sorry, Laya 💔</div>', unsafe_allow_html=True)

st.markdown('<div class="heart">❤️</div>', unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
    Laya, I know I messed up. You’re one of the most important people in my life,<br>
    and hurting you was the last thing I ever wanted to do.<br><br>

    Your smile means the world to me.<br>
    Your silence is killing me. 💔<br><br>

    Please forgive me.<br>
    Let’s fix this together, not stay mad. 🤝
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.subheader("A Small Poem for You 🌸")

st.markdown("""
> In every laugh and every tear,<br>
> You're the one I hold so dear.<br>
> Anger fades but love remains,<br>
> Let’s heal hearts and lose the chains.<br><br>
> I'm sorry, Laya. Truly. Deeply. Always.
""", unsafe_allow_html=True)

# Forgive Button
st.markdown('<div class="forgive">', unsafe_allow_html=True)
if st.button("🤍 Click here if you forgive me 🤍"):
    st.success("YAY! Thank you Laya! 🥹❤️ You’ve made my day.")
    st.balloons()
st.markdown('</div>', unsafe_allow_html=True)
