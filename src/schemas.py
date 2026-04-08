from pydantic import BaseModel
from typing import List, Literal


class QuestionSchema(BaseModel):
    code: str


class IssueSchema(BaseModel):
    type: Literal['BUG', 'STYLE', 'PERFORMANCE']
    message: str
    

class ReviewSchema(BaseModel):
    issues: List[IssueSchema]