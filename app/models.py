from pydantic import BaseModel

class ToolCall(BaseModel):
    name: str
    args: dict
    
class RunBody(BaseModel):
    user_id: str
    agent_id: str
    tool_call: ToolCall

