import streamlit as st
import sys
import os
import re

# ---------------- IMPORT FIX ----------------
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.llm_service import (
    generate_email_summary,
    generate_email_reply,
)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Email Assistant",
    page_icon="📧",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("📧 AI Email Assistant")
st.markdown(
    "Summarize emails and generate AI-powered replies in seconds."
)
st.divider()

# ---------------- SESSION STATE ----------------
if "summary" not in st.session_state:
    st.session_state.summary = ""

if "reply" not in st.session_state:
    st.session_state.reply = ""

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
col1, col2 = st.columns(2)

with col1:
    summarize_btn = st.button(
        "📄 Generate Summary",
        use_container_width=True
    )

with col2:
    reply_btn = st.button(
        "✍️ Generate Reply",
        use_container_width=True
    )


# ---------------- HELPER ----------------
def format_summary(summary: str) -> str:
    """
    Ensures every bullet appears on a separate line,
    even if the model returns them in one sentence.
    """

    summary = summary.strip()

    # Remove common intro lines
    summary = re.sub(
        r"^Here.*?bullet points:\s*",
        "",
        summary,
        flags=re.IGNORECASE | re.DOTALL
    )

    # Split bullets that came back on one line
    summary = summary.replace("• ", "\n• ")
    summary = summary.replace("- ", "\n- ")

    # Remove accidental leading newline
    return summary.strip()


# ---------------- PROCESSING ----------------
if email_text:

    if summarize_btn:
        with st.spinner("Analyzing email..."):
            summary = generate_email_summary(email_text)
            st.session_state.summary = format_summary(summary)

    if reply_btn:
        with st.spinner("Crafting reply..."):
            st.session_state.reply = generate_email_reply(
                email_text,
                tone
            )

# ---------------- OUTPUT ----------------
if st.session_state.summary or st.session_state.reply:

    st.subheader("🤖 AI Output")

    col1, col2 = st.columns(2, gap="large")

    # -------- SUMMARY --------
    with col1:
        with st.container(border=True):
            st.markdown("#### 📄 Summary")

            if st.session_state.summary:
                st.markdown(st.session_state.summary)
            else:
                st.info(
                    "Generate a summary to see it here."
                )

    # -------- REPLY --------
    with col2:
        with st.container(border=True):
            st.markdown("#### ✍️ Suggested Reply")

            if st.session_state.reply:
                st.markdown(st.session_state.reply)

                st.divider()
                st.caption(
                    "📋 Copy from the box below"
                )

                st.code(
                    st.session_state.reply,
                    language=None
                )
            else:
                st.info(
                    "Generate a reply to see it here."
                )