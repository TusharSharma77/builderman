from app.agent.schemas import TaskPlan
from app.services.ai.gemini_client import generate_text


def create_plan(task_prompt: str, repo_map: str) -> TaskPlan:
    prompt = f"""
Create a short coding plan using the task and repository map below.
Return ONLY valid JSON in this exact shape:
{{
  "summary": "plan summary",
  "steps": [
    {{
      "goal": "step goal",
      "files_to_read": ["path"],
      "files_to_edit": ["path"]
    }}
  ]
}}

Task:
{task_prompt}

Repository map:
{repo_map}
"""
    response = generate_text(prompt)
    return TaskPlan.model_validate_json(response)