from app.agent.schemas import TaskPlan
from app.services.ai.gemini_client import generate_text


def create_implementation(
    task_prompt: str,
    repo_map: str,
    plan: TaskPlan,
) -> str:
    prompt = f"""
Produce a proposed unified diff for the coding task below.
Use only the repository information and plan provided. Do not invent file contents.
If there is not enough context to make a reliable change, explain what context is
missing instead of producing a speculative diff.
Return plain text without Markdown code fences. Do not claim to have edited files.

Task:
{task_prompt}

Plan:
{plan.model_dump_json(indent=2)}

Repository map:
{repo_map}
"""
    return generate_text(prompt)
