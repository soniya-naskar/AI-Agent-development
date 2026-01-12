
from fastapi import FastAPI
from pydantic import BaseModel
from rag import get_answer

app = FastAPI()

class AskRequest(BaseModel):
    query: str
    session_id: str | None = None

class AskResponse(BaseModel):
    answer: str
    source: list[str]

@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    answer, sources = get_answer(req.query, req.session_id)
    return AskResponse(answer=answer, source=sources)
