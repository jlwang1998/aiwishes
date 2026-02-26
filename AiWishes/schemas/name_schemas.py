from .agent_schemas import NameSchema
from pydantic import BaseModel, Field, EmailStr, model_validator
from typing import Annotated,Literal,List

class nameIn(BaseModel):
    """姓名生成接口的输入数据模型"""
    surname = Annotated[str, Field(..., description="姓氏")]
    gender: Annotated[Literal["不限", "男", "女"], Field(..., description="性别")]
    length: Annotated[Literal["不限", "单字", "两字"], Field(..., description="字数")]
    other: Annotated[str|None, Field("", description="其他要求")]
    exclude: Annotated[List[str], Field([], description="排除的名字")]

class nameOut(BaseModel):
    """姓名生成接口的输出数据模型"""
    names: List[NameSchema]