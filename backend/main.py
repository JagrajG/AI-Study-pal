import pdf_reader
import prompts
import ai_client
import parser

from fastapi import FastAPI
from random import randint

app = FastAPI()

# file_path = input("Please enter a file path: ")
file_path = "/Users/jagrajgill/Desktop/CODE/projects/AI/AI Flash Cards/Phys190 final.pdf"

# get the text from the file
extracted_text = pdf_reader.extract_text(file_path)

# clean the text from the file
cleaned_text = pdf_reader.clean_text(extracted_text)

#put the cleaned data into a prompt
prompt_text = prompts.construct_prompt(cleaned_text)

flash_cards = ai_client.generate_summary(prompt_text)

# parse json
parsed_flashcards, parse_error = parser.parse_data(flash_cards)

if parse_error:
    print("JSON parse error:", parse_error)
    exit()

#validate parsed data
valid_json, validation_error = parser.validate(parsed_flashcards)

if not valid_json:
    print("JSON validation error:", validation_error)
    exit()

print("JSON is valid!")
print(parsed_flashcards)