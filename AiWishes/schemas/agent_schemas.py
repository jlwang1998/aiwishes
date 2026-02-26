""""为了让大模型的输出内容格式符合需求"""
from pydantic import BaseModel, Field, EmailStr, model_validator
from typing import Annotated,Literal,List

class NameSchema(BaseModel):
    name: Annotated[str, Field(...,description="姓名")]
    reference: Annotated[str, Field(..., description="出处")]
    moral: Annotated[str, Field(..., description="寓意")]

class NameResultSchema(BaseModel):
    names: List[NameSchema]

