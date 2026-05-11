def construct_prompt(data):
    return f"""
Return ONLY valid JSON in the following format:

{{
  "title": "string",
  "flashcards": [
    {{
      "question": "string",
      "answer": "string"
    }},
    {{
      "question": "string",
      "answer": "string"
    }}
  ]
}}

Rules:
- Create exactly 10 flashcards
- Each flashcard must have a question and answer
- Use ONLY the provided text
- Do NOT add any extra text
- Do NOT use markdown
- Do NOT include explanations

Text:
{data}
"""