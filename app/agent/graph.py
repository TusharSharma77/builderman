from langgraph.graph import END, START, StateGraph

from app.agent.implementer import create_implementation
from app.agent.planner import create_plan
from app.agent.schemas import TaskPlan
from app.agent.state import AgentState


def planner_node(state: AgentState) -> dict[str, TaskPlan]:
    plan = create_plan(state["task_prompt"], state["repo_map"])
    return {"plan": plan}


def implementer_node(state: AgentState) -> dict[str, str]:
    plan = state["plan"]
    if plan is None:
        raise ValueError("An implementation cannot be generated without a plan.")

    implementation = create_implementation(
        state["task_prompt"],
        state["repo_map"],
        plan,
    )
    return {"implementation": implementation}


def build_agent_graph():
    builder = StateGraph(AgentState)
    builder.add_node("planner", planner_node)
    builder.add_node("implementer", implementer_node)
    builder.add_edge(START, "planner")
    builder.add_edge("planner", "implementer")
    builder.add_edge("implementer", END)
    return builder.compile()