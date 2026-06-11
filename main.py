
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from app.agents import build_graph

app = FastAPI(title="Ebook Generator API")
graph = build_graph()

class EbookRequest(BaseModel):
    topic: str
    audience: str = "Público geral"
    tone: str = "Profissional"
    num_chapters: int = 3

@app.get("/")
def health():
    return {"status": "online"}

@app.post("/generate")
def generate(req: EbookRequest):
    state = {
        "topic": req.topic, "audience": req.audience,
        "tone": req.tone, "num_chapters": req.num_chapters,
        "outline": {}, "written_chapters": [], "final_html": ""
    }
    graph.invoke(state)
    return FileResponse("ebook.pdf", filename="ebook.pdf")
