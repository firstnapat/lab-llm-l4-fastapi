from http import client
import json
from app.models import GrammarTaskRequest, GrammarTaskResponse

async def process_grammar_task(request: GrammarTaskRequest) -> GrammarTaskResponse:

    system_prompts = """
    You will be presented with user reviews and your job is to provide a set of tags from the following list. Provide your answer in json form with key "tags" and value is set of tags. Choose ONLY from the list of tags provided here (choose either the positive or the negative tag but NOT both):
        - Provides good value for the price OR Costs too much
        - Works better than expected OR Did not work as well as expected
        - Includes essential features OR Lacks essential features
        - Easy to use OR Difficult to use
        - High quality and durability OR Poor quality and durability
        - Easy and affordable to maintain or repair OR Difficult or costly to maintain or repair
        - Easy to transport OR Difficult to transport
        - Easy to store OR Difficult to store
        - Compatible with other devices or systems OR Not compatible with other devices or systems
        - Safe and user-friendly OR Unsafe or hazardous to use
        - Excellent customer support OR Poor customer support
        - Generous and comprehensive warranty OR Limited or insufficient warranty
    """

    def analyze_review(text):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": [{"type": "text", "text": system_prompts}]},
                {"role": "user","content": [{"type": "text", "text": text}]}
            ],
            # TODO-6: set hyperparams
            temperature=0,
            max_tokens=64,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return json.loads(response.choices[0].message.content)
    return GrammarTaskResponse(text="TODO")

