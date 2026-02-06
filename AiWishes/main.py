from fastapi import FastAPI, Depends
from  dependencies import get_mail
from fastapi_mail import FastMail, MessageSchema, MessageType
from aiosmtplib import SMTPResponseException

