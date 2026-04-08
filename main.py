import os

from dotenv import load_dotenv
from openai import OpenAI

from src.promts import code_review_system_promt, code_review_user_promt
from src.schemas import ReviewSchema

load_dotenv()
client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=os.getenv("API_KEY"))


def ask_llm(system_prompt: str, user_prompt: str) -> str:
    response = client.responses.create(
        model="openai/gpt-oss-120b:free",
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


def main():
    
    response = ask_llm(code_review_system_promt, code_review_user_promt)
    print(response)
    print(type(response))
    data = ReviewSchema.model_validate_json(response)
    
    print('\n')
    print(data)
    print(type(data))
    print("\n")
    print(data.model_dump_json())
    print(type(data.model_dump_json()))


if __name__ == "__main__":
    main()
