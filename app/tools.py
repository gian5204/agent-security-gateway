def get_customer(customer_id: str):
    return {"id": customer_id, "name": "gian"}

def delete_customer(customer_id: str):
    return {"deleted": customer_id}

TOOL_PERMISSIONS = {
    "get_customer": "customer.read",
    "delete_customer": "customer.delete",
}

TOOLS = {
    "get_customer": {
        "permission": "customer.read",
        "function": get_customer
    },
    "delete_customer": {
        "permission": "customer.delete",
        "function": delete_customer
    }
}

def tool_exists(name: str) -> bool:
    tool = TOOLS.get(name)
    
    return tool is not None