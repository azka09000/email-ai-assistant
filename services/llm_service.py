import os
import json
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
- Each bullet MUST start with "-"
- Put each bullet on a NEW LINE
- Remove all unnecessary detail
- Focus only on key decisions, actions, and important info
- No explanations, no paragraphs
- Do NOT include any intro or heading text

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


# ---------------- EMAIL CLASSIFICATION (FIXED - JSON OUTPUT) ----------------
def classify_email(email_text: str):
    prompt = f"""
You are an expert email classification system.

TASK:
Classify the email and return ONLY valid JSON.

CATEGORIES:
- Job Opportunity
- Meeting Request
- Task Assignment
- Inquiry
- Spam / Promotional
- General

PRIORITY:
- High
- Medium
- Low

STRICT OUTPUT FORMAT (JSON ONLY):
{{
  "type": "<category>",
  "priority": "<High|Medium|Low>",
  "reason": "<one short sentence>"
}}

RULES:
- Output ONLY JSON
- No extra text
- No explanations
- No markdown
- No bullet points

EMAIL:
{email_text}
"""

    response = client.chat.completions.create(
        model="meta-llama/llama-3.1-8b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    content = response.choices[0].message.content.strip()

    # Safe parsing fallback
    try:
        return json.loads(content)
    except:
        return {
            "type": "General",
            "priority": "Low",
            "reason": content
        }