from pydantic import BaseModel


class PlanStep(BaseModel):
    goal: str
    files_to_read: list[str]
    files_to_edit: list[str]


class TaskPlan(BaseModel):
    summary: str
    steps: list[PlanStep]

        