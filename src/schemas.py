from typing import List, Literal

from pydantic import BaseModel


class QuestionSchema(BaseModel):
    code: str


class IssueSchema(BaseModel):
    type: Literal["BUG", "STYLE", "PERFORMANCE"]
    message: str


class ReviewSchema(BaseModel):
    issues: List[IssueSchema]
