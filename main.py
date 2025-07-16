from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

from google.generativeai import GenerativeModel, configure

api_key = os.getenv('GOOGLE_API_KEY')
configure(api_key=api_key)

model = GenerativeModel('gemini-1.5-flash-latest')

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class CareerRequest(BaseModel):
    question: str

@app.post('/career-buddy')
def ask_career_buddy(request: CareerRequest):
    response = model.generate_content(request.question)
    return {'answer': response.text}
