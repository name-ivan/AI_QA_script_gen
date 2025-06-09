import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

doc_templates = {
    "test_stories": "Write detailed QA test stories based on the following product description:",
    "test_suite": "Write a structured test suite covering major functional areas:",
    "checklist": "Create a clear checklist for manual testing:",
    "bug_report": "Write a realistic bug report for an issue found in the system described below:"
}

def generate_doc(prompt: str, doc_type: str) -> str:
    instruction = doc_templates.get(doc_type, "Write test documentation for this system:")
    full_prompt = f"{instruction}\n\n{prompt}"

    response = client.messages.create(
        model="claude-3-sonnet-20240229",  # Cheaper, balanced Claude 3 model (vs "claude-3-opus-20240229")
        max_tokens=1024,
        temperature=0.7,
        messages=[
            {"role": "user", "content": full_prompt}
        ]
    )


    return response.content[0].text.strip()
