from models import AsyncSession
from models.user import User,EmailCode
from sqlalchemy import select, update, delete, exists
from datetime import datetime, timedelta

class EmailCodeRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    # 异步方法：创建一个新的邮箱验证码记录。它接收两个字符串参数：email（邮箱地址）和code（验证码），返回一个EmailCode对象
    async def create(self, email: str, code: str) -> EmailCode:
        async with self.session.begin():
            email_code = EmailCode(email=email, code=code)
            # 将新创建的EmailCode对象添加到数据库会话中。这标记对象为待保存，但实际保存到数据库可能在事务提交时发生
            self.session.add(email_code)
            return email_code
        
    # 异步方法：验证给定邮箱和验证码的有效性。它接收两个字符串参数：email（邮箱地址）和code（验证码），返回一个布尔值，表示验证码是否有效
    async def check_email_code(self, email: str, code: str) -> bool:
        async with self.session.begin():
            email_code:EmailCode|None = await self.session.scalar(
                select(EmailCode).filter(EmailCode.email == email, EmailCode.code == code))

            if not email_code:
                return False
            # 检查验证码是否在有效期内（5分钟）
            if(datetime.now() - email_code.created_time) > timedelta(minutes=5):
                return False
            return True