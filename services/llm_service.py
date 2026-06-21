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
You are an expert email summarizer.

TASK:
Convert the email into a SHORT EXECUTIVE SUMMARY.

STRICT RULES:
- 5 to 7 bullet points only
- Each bullet must be short (max 15 words)
- Remove all unnecessary detail
- Do NOT copy full sections of the email
- Focus only on key decisions, actions, and important info
- No explanations, no paragraphs

OUTPUT FORMAT:
- Bullet points only

EMAIL:
{email_text}
"""

    response = client.chat.completions.create(
        model="meta-llama/llama-3.1-8b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()


# ---------------- REPLY ----------------
def generate_email_reply(email_text: str, tone: str = "professional"):
    prompt = f"""
You are an expert email writer.

TASK:
Write a {tone} email reply.

STRICT RULES:
- Keep reply concise and natural
- No unnecessary explanations
- Professional structure (greeting + body + closing)
- 120–180 words maximum
- Do NOT repeat the original email
- Make it ready to send as-is

EMAIL:
{email_text}
"""

    response = client.chat.completions.create(
        model="meta-llama/llama-3.1-8b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content.strip()