import json
def validate(data):
    if not isinstance(data, dict):
        return False, "Data must be a dictionary"
    
    if "title" not in data or not isinstance(data["title"], str):
        return False, "Invalid or missing title"
    
    if "flashcards" not in data or not isinstance(data["flashcards"], list):
        return False, "Invalid or missing flashcards"
    
    if len(data["flashcards"]) != 10:
        return False, "Must have exactly 10 flashcards"
    
    for card in data["flashcards"]:
        if not isinstance(card, dict):
            return False, "Each flashcard must be a dictionary"
        
        if "question" not in card or not isinstance(card["question"], str):
            return False, "Invalid or missing question"
        
        if not card["question"].strip():
            return False, "Question cannot be empty"
        
        if "answer" not in card or not isinstance(card["answer"], str):
            return False, "Invalid or missing answer"
        
        if not card["answer"].strip():
            return False, "Answer cannot be empty"
        
        if len(card["answer"]) < 10:
            return False, "Answer too short (likely incomplete)"
    
    return True, None

def parse_data(response_text):
    try:
        parsed_json = json.loads(response_text)
        return parsed_json, None
    except json.JSONDecodeError:
        return None, "Error: JSON failed to load"