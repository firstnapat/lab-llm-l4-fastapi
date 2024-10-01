
import os
from openai import OpenAI
from app.models import GrammarTaskRequest, GrammarTaskResponse

async def process_grammar_task(request: GrammarTaskRequest) -> GrammarTaskResponse:
    client = OpenAI(api_key=os.getenv("OAI_KEY"))
    style_prompts = {
        "informal": "Using informal words like talking to a friend.",
        "ielts": "Using very fancy words.",
        "formal": "Using formal words.",
        "acedemic": "Using academic words suitable for academic publications.",
        "default": ""
    }

    text = request.text
    style = request.style

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[

        {
            "role": "system",
            "content": f"You will be provided with statements, and your task is to convert them to standard English. {style_prompts[style]}"
        },
        {
            "role": "user",
            "content": text
        }
    ],
        temperature=0.7,
        max_tokens=64,
        top_p=1
    )
    return {"text": response.choices[0].message.content}

