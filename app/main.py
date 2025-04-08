from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

app = FastAPI()

ModelId = "distilbert/distilgpt2"

tokenizer = AutoTokenizer.from_pretrained(ModelId)
model = AutoModelForCausalLM.from_pretrained(ModelId)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

class prompt(BaseModel):
    text: str

@app.post("/generate")
def generate(prompt: prompt):
    result = generator(prompt.text, max_new_tokens=100)
    return {"result": result[0]["generated_text"]}