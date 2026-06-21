import streamlit as st
from services.llm_service import generate_email_summary, generate_email_reply

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Email Assistant",
    page_icon="📧",
    layout="wide"
)

st.title("📧 AI Email Assistant")
st.markdown("Paste an email and get AI-powered summary + reply")

st.divider()

# ---------------- INPUT ----------------
email_text = st.text_area("✉️ Paste Email", height=250)

tone = st.selectbox("Select Reply Tone", ["professional", "friendly", "concise"])

# ---------------- BUTTONS ----------------
col1, col2 = st.columns(2)

with col1:
    summarize_btn = st.button("📄 Summarize Email")

with col2:
    reply_btn = st.button("✍️ Generate Reply")

# ---------------- OUTPUT ----------------
if email_text:

    if summarize_btn:
        with st.spinner("Generating summary..."):
            summary = generate_email_summary(email_text)
            st.subheader("📄 Summary")
            st.write(summary)

    if reply_btn:
        with st.spinner("Generating reply..."):
            reply = generate_email_reply(email_text, tone)
            st.subheader("✍️ Suggested Reply")
            st.write(reply)