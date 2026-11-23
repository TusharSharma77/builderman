from langgraph.graph import END, START, StateGraph

from app.agent.planner import create_plan
from app.agent.schemas import TaskPlan
from app.agent.state import AgentState


def planner_node(state: AgentState) -> dict[str, TaskPlan]:
    plan = create_plan(state["task_prompt"], state["repo_map"])
    return {"plan": plan}


def build_agent_graph():
    builder = StateGraph(AgentState)
    builder.add_node("planner", planner_node)
    builder.add_edge(START, "planner")
    builder.add_edge("planner", END)
    return builder.compile()