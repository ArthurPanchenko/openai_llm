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
    llm_response = await llm_service.ask_llm(data.code)
    
    response = ReviewSchema.model_validate_json(llm_response)
    
    return response
    
