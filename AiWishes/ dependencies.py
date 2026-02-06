from core.mail import create_mail_instance
from fastapi_mail import FastMail



# 获取邮件实例，异步
async def get_mail() -> FastMail:
    return create_mail_instance()
