from fastapi import APIRouter
from agents.langgraph_agent import run_agent

router=APIRouter()

@router.post("/chat")

def chat(data:dict):

    message=data["message"]

    result=run_agent(message)

    return result