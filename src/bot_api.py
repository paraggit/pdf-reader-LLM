from transformers import GPT2Tokenizer, GPT2LMHeadModel
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

tokenizer = GPT2Tokenizer.from_pretrained("./models/fine_tuned_model")
model = GPT2LMHeadModel.from_pretrained("./models/fine_tuned_model")


@app.post("/ask")
async def ask_bot(request: Request):
    data = await request.json()
    question = data.get("question")
    inputs = tokenizer.encode(question, return_tensors="pt")
    outputs = model.generate(inputs, max_length=500, num_return_sequences=1)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"answer": answer}


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
