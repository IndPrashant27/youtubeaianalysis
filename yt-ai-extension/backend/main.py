from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transcript_utils import get_transcript_from_url
from vector_utils import build_vector_store, get_answer

app = FastAPI()

# ✅ Add CORS middleware BEFORE defining routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to specific domains later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    video_url: str
    question: str

@app.post("/ask")
def ask(req: AskRequest):
    transcript_text = get_transcript_from_url(req.video_url)
    vector_store = build_vector_store(transcript_text)
    answer = get_answer(vector_store, req.question)
    return {"answer": answer}
