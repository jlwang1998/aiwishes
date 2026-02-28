from fastapi import FastAPI, Depends
from fastapi_mail import FastMail, MessageSchema, MessageType
from aiosmtplib import SMTPResponseException
from dependencies import get_mail
from routers.auth_router import router as auth_router
from routers.agent_router import router as name_router


app = FastAPI()
app.include_router(auth_router)
app.include_router(name_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

#测试邮件发送
#http://127.0.0.1:8000/mail/test?email=jlwang1998@163.com
@app.get('/mail/test')
async def send_mail_test(
    email: str,
    mail: FastMail = Depends(get_mail) #fastapi依赖注入
):
    message = MessageSchema(
    subject="hello",               # 邮件主题
    recipients=[email],            # 收件人列表（可多个）
    body=f"Hello {email}",         # 邮件正文
    subtype=MessageType.plain      # 邮件类型：纯文本
    )
    try:
        await mail.send_message(message)
    except SMTPResponseException as e:
        if e.code == -1 and b"\\x00\\x00\\x00" in str(e).encode():
            print("⚠️ 忽略 QQ 邮箱 SMTP 关闭阶段的非标准响应（邮件已成功发送）")
    return {"message": "邮件发送成功！"}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
