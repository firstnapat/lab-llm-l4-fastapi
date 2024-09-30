from fastapi import APIRouter
from app.models import GrammarTaskRequest, GrammarTaskResponse
from app.services.grammar_service import process_grammar_task

router = APIRouter()

@router.post("/openai/grammar", response_model=GrammarTaskResponse)
async def openai_grammar(request: GrammarTaskRequest) -> GrammarTaskResponse:
    result = await process_grammar_task(request)
    return result

