from fastapi import FastAPI
from pydantic import BaseModel

class RunBody(BaseModel):
    user_id: str
    agent_id: str
    prompt: str

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/agents/run")
async def run_agent(body: RunBody):
    return body
