from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware

# Create a new FastAPI app instance
app = FastAPI()

# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize the text generation pipeline
pipe = pipeline("text2text-generation", model="google/flan-t5-small")

class TextInput(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Welcome to the Text Generation API"}

@app.post("/generate")
def generate(input: TextInput):
    # Use pipeline to generate text from given text as input param
    output = pipe(input.text)
    # Return the generated text in JSON response
    return {"output": output[0]['generated_text']}
