"""用于存放和用户操作相关的路由，并添加获取邮箱验证码的视图函数代码"""

from fastapi import APIRouter, Query, Depends, HTTPException
from pydantic import EmailStr
from typing import Annotated
from dependencies import get_mail, get_session
from fastapi_mail import FastMail, MessageSchema, MessageType
from models import AsyncSession
import string
import random
from aiosmtplib import SMTPResponseException
from repository.user_repo import EmailCodeRepository, User, UserRepository
from schemas import ResponseOut


router = APIRouter(prefix="/auth")

# - response_model=ResponseOut：指定响应数据的模型为ResponseOut，FastAPI会自动将返回值转换为该模型格式
@router.get("/code", response_model=ResponseOut)
async def get_email_code(
     # 定义查询参数email，使用Annotated和Query进行注解
     # - EmailStr：Pydantic的邮箱格式验证类型，确保传入的字符串是有效的邮箱格式
     # - Query(...)：FastAPI的Query参数，省略号(...)表示该参数是必需的，如果请求中缺少将返回错误
     # 综合作用：从查询参数中获取邮箱地址，并验证其格式。例如：GET /auth/code?email=user@example.com
     # 类型注解：Annotated[...]- 这是Python 3.9+引入的注解语法（在旧版Python中可从typing_extensions导入）。它允许为类型添加元数据（metadata）。
     # 基本语法是：Annotated[类型, 元数据1, 元数据2, ...]
     # 在Query(...)中，省略号表示该参数是必需的（required）。如果请求中不提供该参数，FastAPI会自动返回422错误响应，提示参数缺失。
    email: Annotated[EmailStr, Query(...)],
    mail: FastMail = Depends(get_mail),
    session: AsyncSession = Depends(get_session),

):
    source = string.digits * 4
    code = "".join(random.sample(source, 4))
    # - subtype：邮件内容类型，MessageType.plain表示纯文本格式（无HTML）
    message = MessageSchema(
        subject="【aiwishes】注册验证码",
        recipients=[email],
        body=f"您的验证码为：{code}，五分钟有效！",
        subtype=MessageType.plain
    )
    #发送邮件
    try:
        print(f"正在发送验证码邮件到 {email}，验证码为：{code}")
        await mail.send_message(message)
        # 邮件发送成功，保存验证码到数据库
        email_code_repo = EmailCodeRepository(session)
        await email_code_repo.create(email=str(email), code=code)
    except SMTPResponseException as e:
        if e.code == -1 and b"\\x00\\x00\\x00" in str(e).encode():
            print("⚠️ 忽略 QQ 邮箱 SMTP 关闭阶段的非标准响应（邮件已成功发送）")
            ## 创建EmailCodeRepository实例，传入数据库会话，并调用create方法保存邮箱和验证码到数据库
            email_code_repo = EmailCodeRepository(session=session)
            await email_code_repo.create(str(email), code)
        else:
            raise HTTPException(500, detail="邮件发送失败！")
    return ResponseOut()