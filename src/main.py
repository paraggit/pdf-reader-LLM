import argparse
from pdf_reader import extract_text_from_pdfs
from preprocess import preprocess_text
from fine_tune import fine_tune_model

def main():
    parser = argparse.ArgumentParser(description="Process PDF files for text extraction and model fine-tuning.")
    parser.add_argument('pdf_directory', type=str, help='Path to the directory containing PDF files')
    args = parser.parse_args()

    pdf_directory = args.pdf_directory

    # Extract text from PDFs
    pdf_texts = extract_text_from_pdfs(pdf_directory)

    # Preprocess the extracted text
    preprocessed_texts = [preprocess_text(text) for text in pdf_texts]

    # Fine-tune the language model
    fine_tune_model(preprocessed_texts, output_dir='./models/fine_tuned_model')

if __name__ == "__main__":
    main()
