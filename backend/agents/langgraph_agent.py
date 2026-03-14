from langgraph.graph import StateGraph
from tools.summarize_interaction import summarize_interaction
from tools.suggest_followups import suggest_followups
from tools.log_interaction import log_interaction

class State(dict):
    pass


def summarize_node(state):

    text=state["input"]

    summary=summarize_interaction(text)

    state["summary"]=summary

    return state


def followup_node(state):

    followups=suggest_followups(state["input"])

    state["followups"]=followups

    return state


def save_node(state):

    log_interaction(state["summary"])

    return state


def build_graph():

    graph=StateGraph(State)

    graph.add_node("summarize",summarize_node)

    graph.add_node("followups",followup_node)

    graph.add_node("save",save_node)

    graph.set_entry_point("summarize")

    graph.add_edge("summarize","followups")

    graph.add_edge("followups","save")

    return graph.compile()


workflow=build_graph()


def run_agent(text):

    return workflow.invoke({"input":text})