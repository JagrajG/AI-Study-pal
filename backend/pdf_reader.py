import pymupdf


def extract_text(file_path):
    doc_data = []

    with pymupdf.open(file_path) as doc:
        for page in doc:
            text = page.get_text()
            doc_data.append(text)

    return "\n".join(doc_data)


def clean_text(text):
    cleaned = text.replace("\n", " ")
    cleaned = " ".join(cleaned.split())
    return cleaned[:3000]