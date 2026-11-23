from typing import TypedDict


from app.agent.schemas import TaskPlan


class AgentState(TypedDict):
    task_prompt: str
    repo_map: str
    plan: TaskPlan | None