from . import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, DateTime
from pwdlib import PasswordHash
from datetime import datetime
from . import user

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    username: Mapped[str] = mapped_column(String(100))
    # 私有字段，存储哈希后的密码，字符串类型最大长度200
    _password: Mapped[str] = mapped_column(String(100))

    """
    *args：可以接收任何数量的普通信息
    **kwargs：可以接收任何数量的带名字的信息"""
    def __init__(self, *args, **kwargs):
        password = kwargs.get("password")
        if password:
            password = kwargs.pop("password")
        #使用父类方法初始化参数
        super().__init__(*args, **kwargs)
        self.password = password#触发setter方法
        #@property是Python的魔法装饰器，它会把方法变成属性
        @property
        def password(self):
            return self._password
        
        @password.setter
        def password(self, password):
            self._password = PasswordHash().hash(password)

        def check_password(self, password):
            return PasswordHash().verify(password, self._password)
        
class EmailCode(Base):
    __tablename__ = "email_code"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(100))
    code: Mapped[str] = mapped_column(String(10))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    
    