from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI(title="Générateur IA API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    user_input: str

@app.get("/")
def read_root():
    return {"status": "online", "message": "L'API fonctionne !"}

@app.post("/generate")
async def generate_response(request: PromptRequest):
    if not request.user_input:
        raise HTTPException(status_code=400, detail="Texte vide.")
    try:
        response_text = f"Analyse de : '{request.user_input}'. Traitement en cours..."
        return {"success": True, "result": response_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
