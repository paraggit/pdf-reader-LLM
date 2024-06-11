# PDF Answering Bot

This project is a PDF Answering Bot that reads all PDFs from a given location, processes the text, fine-tunes a language model, and deploys it as an answering bot using FastAPI.

## Project Structure

src/
│
├── main.py
├── pdf_reader.py
├── preprocess.py
├── fine_tune.py
├── bot_api.py
│
└── models/
└── fine_tuned_model


- `main.py`: Entry point of the application. Extracts, preprocesses text from PDFs, and fine-tunes the language model.
- `pdf_reader.py`: Module for reading and extracting text from PDFs.
- `preprocess.py`: Module for preprocessing the extracted text.
- `fine_tune.py`: Module for fine-tuning the language model.
- `bot_api.py`: Module to set up the FastAPI server for the answering bot.
- `models/fine_tuned_model/`: Directory where the fine-tuned model will be saved.

## Requirements

Install the necessary packages using pip:

```bash
pip install PyMuPDF transformers torch fastapi uvicorn

##Usage
###Step 1: Extract, Preprocess, and Fine-tune the Model

Run the main.py script to extract text from PDFs, preprocess it, and fine-tune the language model:

#> python main.py

##Step 2: Start the API

Run the bot_api.py script to start the FastAPI server:

#> python bot_api.py

##API Endpoint

Once the server is running, you can interact with the bot by sending POST requests to http://localhost:8000/ask with a JSON payload containing the question.
Example POST Request

You can use tools like curl or Postman to test your API:
 #> curl -X POST "http://localhost:8000/ask" -H "Content-Type: application/json" -d '{"question": "What is the summary of the document?"}'

