from pydantic import BaseModel, Field, EmailStr, model_validator
from typing import Annotated,Literal,List
from .agent_schemas import WishSchema


class WishIn(BaseModel):
    """祝福语生成接口的输入数据模型"""
    name: Annotated[str, Field(..., description="姓名")]
    gender: Annotated[Literal["不限", "男", "女"], Field(..., description="性别")]
    relation: Annotated[str, Field(..., description="关系")]
    wish_type: Annotated[str, Field(..., description="祝语类型")] #节日、生日、结婚等
    wish_style: Annotated[str, Field(..., description="祝语风格")] #幽默、正式、温馨等
    wish_length: Annotated[int, Field(..., description="祝语长度")] 

class WishOut(BaseModel):
    """祝福语生成接口的输出数据模型"""
    wishes: List[WishSchema]