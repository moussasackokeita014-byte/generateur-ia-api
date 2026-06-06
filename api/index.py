
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import anthropic
import os

app = FastAPI(title="ReussirGN API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

class Question(BaseModel):
    classe: str
    matiere: str
    question: str

@app.get("/")
def home():
    return {"status": "online", "message": "ReussirGN API fonctionne !"}

@app.post("/ask")
def ask(q: Question):
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="Tu es ReussirGN, un assistant scolaire guinéen.",
        messages=[{"role": "user", "content": f"Classe: {q.classe}\nMatière: {q.matiere}\nQuestion: {q.question}"}]
    )
    return {"reponse": message.content[0].text}
