from fastapi import FastAPI, HTTPException

from app.auth import can_use_tool
from app.tools import TOOLS, tool_exists
from app.models import RunBody

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/agents/run")
async def run_agent(body: RunBody):
    tool = body.tool_call.name

    if not tool_exists(tool):
        raise HTTPException(
            status_code=404,
            detail=f"tool {tool} not found"
        )

    if not can_use_tool(body.agent_id, tool):
        raise HTTPException(
            status_code=403,
            detail=f"insufficient permissions to run tool {tool}"
        )

    return TOOLS[tool]["function"](**body.tool_call.args)

