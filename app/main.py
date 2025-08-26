from fastapi import FastAPI
import os
import google.generativeai as genai

app = FastAPI()

API_KEY = os.getenv("GEMINI_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

@app.get("/healthz")
def health():
    return {"ok": True}

@app.get("/")
def root():
    return {"service": "web-api", "env": os.getenv("ENV", "local")}

@app.get("/ask")
def ask(q: str):
    if not API_KEY:
        return {"error": "Gemini API key not configured"}
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(q)
    return {"question": q, "answer": response.text}
  
