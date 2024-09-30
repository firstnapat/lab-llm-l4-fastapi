from pydantic import BaseModel
from typing import Optional

class GrammarTaskRequest(BaseModel):
    text: str
    style: Optional[str] = "default"

class GrammarTaskResponse(BaseModel):
    text: str

