import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


# ---------------- SUMMARY ----------------
def generate_email_summary(email_text: str):
    prompt = f"""
Summarize this email into clear bullet points:

{email_text}
"""

    response = client.chat.completions.create(
        model="meta-llama/llama-3.1-8b-instruct",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# ---------------- REPLY ----------------
def generate_email_reply(email_text: str, tone: str = "professional"):
    prompt = f"""
Write a {tone} email reply to the following email:

{email_text}
"""

    response = client.chat.completions.create(
        model="meta-llama/llama-3.1-8b-instruct",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content