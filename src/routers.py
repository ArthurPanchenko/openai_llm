from fastapi import HTTPException
from fastapi.routing import APIRouter

from src.schemas import QuestionSchema
from src.ai_service.llm_service import llm_service
from src.schemas import ReviewSchema

api_router = APIRouter()


@api_router.get('/')
async def index():
    return {'status': 'ok'}
    

@api_router.post('/review', response_model=ReviewSchema)
async def review(data: QuestionSchema):

    return await llm_service.ask_and_parse(data.code)

    
