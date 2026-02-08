from core.mail import create_mail_instance
from fastapi_mail import FastMail
from models import AsyncSessionFactory
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator


"""简单理解：
如果一个函数有 yield关键字，它就是生成器函数
生成器函数的返回类型应该标注为生成器类型，而不是普通类型
源代码async def get_session() -> AsyncSession:返回的类型不对，报错

"""
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    session = AsyncSessionFactory()
    try:
        yield session ## 有yield，说明这是生成器函数
    finally:
        await session.close()



# 获取邮件实例，异步
async def get_mail() -> FastMail:
    return create_mail_instance()
