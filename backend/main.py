import os
import tempfile

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

import pdf_reader
import prompts
import ai_client
import parser

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Backend is running"}


@app.post("/generate-flashcards")
async def generate_flashcards(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        return {"error": "Please upload a PDF file"}

    temp_path = None

    try:
        contents = await file.read()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(contents)
            temp_path = temp_file.name

        extracted_text = pdf_reader.extract_text(temp_path)
        cleaned_text = pdf_reader.clean_text(extracted_text)

        prompt_text = prompts.construct_prompt(cleaned_text)
        ai_response = ai_client.generate_summary(prompt_text)

        parsed_flashcards, parse_error = parser.parse_data(ai_response)

        if parse_error:
            return {"error": parse_error, "raw_response": ai_response}

        valid_json, validation_error = parser.validate(parsed_flashcards)

        if not valid_json:
            return {"error": validation_error, "raw_response": ai_response}

        return parsed_flashcards

    except Exception as e:
        return {"error": str(e)}

    finally:
        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)