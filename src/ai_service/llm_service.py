from openai import OpenAI

from config import settings
from src.ai_service.promts import code_review_system_promt, create_code_review_user_prompt  # code_review_user_promt
from src.schemas import ReviewSchema


class LLMService:
    
    def __init__(self):
        
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1", api_key=settings.API_KEY
        )
    
    async def ask_llm(self, user_prompt: str, system_prompt: str | None = None) -> str:
        
        if not system_prompt:
            system_prompt = code_review_system_promt
            
        user_prompt = create_code_review_user_prompt(user_prompt)
        response = self.client.responses.create(
            model=settings.MODEL_TITLE,
            input=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            text={
                "format": {
                    "type": "json_schema",
                    "name": "code_review",
                    "schema": ReviewSchema.model_json_schema(),
                }
            },
        )
        return response.output_text


llm_service = LLMService()
# def main():

#     response = ask_llm(code_review_system_promt, code_review_user_promt)
#     print(response)
#     print(type(response))
#     data = ReviewSchema.model_validate_json(response)

#     print('\n')
#     print(data)
#     print(type(data))
#     print("\n")
#     print(data.model_dump_json())
#     print(type(data.model_dump_json()))
