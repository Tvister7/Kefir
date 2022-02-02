from pydantic import BaseModel
from typing import List


class ValidationError(BaseModel):
    loc: List[str]
    msg: str
    type: str


class HTTPValidationError(BaseModel):
    detail: List[ValidationError]


class ErrorResponseModel(BaseModel):
    code: int
    message: str
