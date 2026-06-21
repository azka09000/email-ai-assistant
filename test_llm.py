from services.llm_service import generate_email_summary

text = "Hello, I want to reschedule our meeting to next week."

print(generate_email_summary(text))