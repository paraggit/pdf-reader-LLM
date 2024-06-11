import fitz  # PyMuPDF
import os


def extract_text_from_pdfs(pdf_directory):
    text_data = []
    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            filepath = os.path.join(pdf_directory, filename)
            with fitz.open(filepath) as doc:
                text = ""
                for page in doc:
                    text += page.get_text()
                text_data.append(text)
    return text_data
