from app.tools import TOOLS
from app.data import AGENTS

def get_agent_perms(agent_id: str) -> set[str]:
    agent = AGENTS.get(agent_id)

    if agent is None:
        return set()
    
    return agent["permissions"]

def can_use_tool(agent_id: str, tool_name: str) -> bool:
    tool = TOOLS.get(tool_name)

    if tool is None:
        return False

    required_permission = tool["permission"]
    
    permissions = get_agent_perms(agent_id)

    return required_permission in permissions