from . import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, DateTime
from pwdlib import PasswordHash
from datetime import datetime

password_hash = PasswordHash.recommended()

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    username: Mapped[str] = mapped_column(String(100))
    # 私有字段，存储哈希后的密码，字符串类型最大长度200
    _password: Mapped[str] = mapped_column(String(200))

    """
    *args：可以接收任何数量的普通信息
    **kwargs：可以接收任何数量的带名字的信息"""
    def __init__(self, *args, **kwargs):
        password = kwargs.pop('password')
        super().__init__(*args, **kwargs)
        if password:
            self.password = password
    #@property是Python的魔法装饰器，它会把方法变成属性
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, raw_password):
        self._password = password_hash.hash(raw_password)

    def check_password(self, raw_password):
        return password_hash.verify(raw_password, self.password)
        
class EmailCode(Base):
    __tablename__ = "email_code"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(100))
    code: Mapped[str] = mapped_column(String(10))
    created_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
