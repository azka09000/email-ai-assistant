import streamlit as st
import sys
import os
import re

# ---------------- IMPORT FIX ----------------
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.llm_service import (
    generate_email_summary,
    generate_email_reply,
    classify_email
)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Email Assistant",
    page_icon="📧",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("📧 AI Email Assistant")
st.markdown("AI-powered email understanding: classify, summarize, and reply")
st.divider()

# ---------------- SESSION STATE ----------------
if "summary" not in st.session_state:
    st.session_state.summary = ""

if "reply" not in st.session_state:
    st.session_state.reply = ""

if "classification" not in st.session_state:
    st.session_state.classification = None

# ---------------- INPUT ----------------
st.subheader("✉️ Email Input")

email_text = st.text_area(
    "Paste Email",
    height=220,
    placeholder="Paste your email here..."
)

tone = st.selectbox(
    "Reply Tone",
    ["professional", "friendly", "concise"]
)

# ---------------- BUTTONS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    summarize_btn = st.button("📄 Generate Summary", use_container_width=True)

with col2:
    reply_btn = st.button("✍️ Generate Reply", use_container_width=True)

with col3:
    classify_btn = st.button("📊 Detect Email Type", use_container_width=True)

# ---------------- PROCESSING ----------------
if email_text:

    if summarize_btn:
        with st.spinner("Analyzing email..."):
            summary = generate_email_summary(email_text)
            st.session_state.summary = summary

    if reply_btn:
        with st.spinner("Crafting reply..."):
            st.session_state.reply = generate_email_reply(
                email_text,
                tone
            )

    if classify_btn:
        with st.spinner("Detecting email type..."):
            st.session_state.classification = classify_email(email_text)

# ---------------- OUTPUT ----------------
if (
    st.session_state.summary
    or st.session_state.reply
    or st.session_state.classification
):

    st.subheader("🤖 AI Output")

    # ---------------- CLASSIFICATION ----------------
    if st.session_state.classification:
        c = st.session_state.classification

        with st.container(border=True):
            st.markdown("### 📊 Email Analysis")

            st.markdown(f"""
**Type:** {c.get("type", "N/A")}  

**Priority:** {c.get("priority", "N/A")}  

**Reason:** {c.get("reason", "N/A")}
            """)

        st.divider()

    col1, col2 = st.columns(2, gap="large")

    # -------- SUMMARY --------
    with col1:
        with st.container(border=True):
            st.markdown("#### 📄 Summary")

            if st.session_state.summary:
                summary = st.session_state.summary

                # bullet fix (safe formatting)
                summary = summary.replace("• ", "\n• ").replace("- ", "\n- ")

                st.markdown(summary)
            else:
                st.info("Generate a summary to see it here.")

    # -------- REPLY --------
    with col2:
        with st.container(border=True):
            st.markdown("#### ✍️ Suggested Reply")

            if st.session_state.reply:
                st.markdown(st.session_state.reply)

                st.divider()
                st.caption("📋 Copy from the box below")

                st.code(
                    st.session_state.reply,
                    language=None
                )
            else:
                st.info("Generate a reply to see it here.")