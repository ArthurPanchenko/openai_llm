from openai import OpenAI
from pydantic import ValidationError

from config import settings
from src.ai_service.exceptions import (
    EmptyLLMOutputError,
    LLMError,
    LLMStructuredOutputError,
)
from src.ai_service.promts import ( 
    code_review_system_promt,
    create_code_review_user_prompt,
)
from src.schemas import ReviewSchema


class LLMService:
    def __init__(self):

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1", api_key=settings.API_KEY
        )
        
    async def ask_llm(self, user_prompt: str, system_prompt: str):
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
        return response

    async def prepare_and_ask_llm(self, user_prompt: str, system_prompt: str | None = None) -> str:

        if not system_prompt:
            system_prompt = code_review_system_promt

        user_prompt = create_code_review_user_prompt(user_prompt)

        try:
            response = await self.ask_llm(user_prompt, system_prompt)
        except LLMError:
            try:
                response = await self.ask_llm(user_prompt, system_prompt)
            except Exception as e:
                raise LLMError(f"Provider request failed: {e}")

        raw_text = response.output_text

        if not raw_text or not raw_text.strip():
            
            raise EmptyLLMOutputError("Model returned empty output")

        return response.output_text

    async def ask_and_parse(
        self, user_prompt: str, system_prompt: str | None = None
    ) -> ReviewSchema:

        raw_llm_response = await self.ask_llm(user_prompt, system_prompt)
        # raw_llm_response = raw_llm_response[:-1]

        try:
            return ReviewSchema.model_validate_json(raw_llm_response)
        except ValidationError as e:
            raise LLMStructuredOutputError(
                message=f"Structured output validation failed: {e}",
                raw_output=raw_llm_response,
                user_prompt=user_prompt,
            )


llm_service = LLMService()