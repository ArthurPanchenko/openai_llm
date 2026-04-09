from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.ai_service.exceptions import LLMError
from src.routers import api_router

app = FastAPI()

app.include_router(api_router)


@app.exception_handler(LLMError)
def llm_error_exception_handler(request: Request, exc: LLMError):
    return JSONResponse(status_code=500, content={"message": str(exc)})
