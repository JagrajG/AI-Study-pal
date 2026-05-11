import pymupdf

def extract_text(file_path):
    doc = pymupdf.open(file_path)

    doc_data = []

    for page in doc:
        text = page.get_text()
        doc_data.append(text)
    doc.close()
    return "\n".join(doc_data)

def clean_text(raw_text):
    text = raw_text.replace("\n", " ")
    text = " ".join(text.split())
    return text[:3000]