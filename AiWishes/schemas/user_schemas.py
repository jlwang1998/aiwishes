"""用来约束和校验前端上传的数据"""
from pydantic import BaseModel, Field, EmailStr, model_validator
from typing import Annotated,Literal,List

UsernameStr = Annotated[str, Field(...,min_length=4, max_length=20, description="用户名")]
RawPasswordStr = Annotated[str, Field(...,min_length=6, max_length=20, description="密码")]
codeStr = Annotated[str, Field(...,min_length=4, max_length=4, description="验证码")]

class RegisterIn(BaseModel):
    """注册接口的输入数据模型"""
    email: EmailStr
    username:UsernameStr
    password: RawPasswordStr
    confirm_password: RawPasswordStr
    code:codeStr

# 模型级验证器：在所有字段验证之后执行，用于检查密码一致性
    # @model_validator(mode="after")：装饰器表示这是一个模型验证器
    # - mode="after"：表示在所有字段验证完成后执行
    # 另一种模式是"before"，表示在字段验证前执行
    @model_validator(mode='after')
    def password_is_match(self)->RegisterIn:
        if self.password != self.confirm_password:
            raise ValueError("两次输入的密码不一致")
        return self

class UserCreateSchema(BaseModel):
    """用户创建的模型"""
    email: EmailStr
    username: UsernameStr
    password: RawPasswordStr

class LoginIn(BaseModel):
    """登录接口的输入数据模型"""
    email: EmailStr
    password: RawPasswordStr

class LoginOut(BaseModel):
    """登录接口的输出数据模型"""
    user: UserCreateSchema
    token: str

