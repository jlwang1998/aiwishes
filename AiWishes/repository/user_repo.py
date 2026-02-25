from models import AsyncSession
from models.user import User,EmailCode
from sqlalchemy import select, update, delete, exists
from datetime import datetime, timedelta
from schemas.user_schemas import UserCreateSchema
class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    # 异步方法：根据邮箱查询用户
    # 参数 email: str - 要查询的邮箱地址
    # 返回值 User|None - 返回查询到的User对象，如果不存在则返回None
    async def get_by_email(self, email: str) -> User | None:
        async with self.session.begin():
            # 执行查询：选择User表，按邮箱过滤
            # 1. select(User): 构建查询，选择User表的所有字段
            # 2. .where(User.email==email): 添加WHERE条件，过滤指定邮箱
            #    - 注意：.where()是SQLAlchemy 2.0推荐的新语法，与.filter()功能相同
            #    - 在旧版本SQLAlchemy中常用.filter()，两者可互换
            # 3. self.session.scalar(): 执行查询并返回单个标量结果
            #    - 查询到结果时返回User对象
            #    - 未查询到结果时返回None
            # 4. await: 等待异步查询完成
            user = await self.session.scalar(select(User).where(User.email==email))
            return user
    # 异步方法：检查邮箱是否已存在
    async def email_is_exist(self, email: str) -> bool:
        async with self.session.begin():
            # 构建存在性查询语句
            # 1. exists(): 创建存在性检查子查询
            # 2. .where(User.email==email): 设置子查询条件
            # 3. stmt = select(exists()...): 将子查询包装在SELECT语句中
            # 这种方法比直接查询完整用户对象更高效，数据库只需返回True/False
            # 1. exists() 函数
            #    - 这是SQLAlchemy的核心函数，用于创建一个SQL EXISTS子查询
            #    - EXISTS是SQL标准操作符，用于检查子查询是否返回任何行
            #    - 语法：SELECT EXISTS(SELECT ... FROM ... WHERE ...)
            #    - 如果子查询返回至少一行，则返回True；否则返回False
            stmt = select(exists().where(User.email==email))
            return await self.session.scalar(stmt)
    # 异步方法：创建新用户
    async def create(self, user_schema: UserCreateSchema) -> User:
        async with self.session.begin():
            # 将Pydantic模型转换为数据库模型
            # 1. user_schema.model_dump(): 将Pydantic模型转换为字典
            #    - 这是Pydantic V2的方法，等同于V1的.dict()
            #    - 转换后的字典包含模型的所有字段数据
            # 2. User(**...): 使用字典解包创建User对象
            #    - 假设User模型的字段名与UserCreateSchema一致
            #    - 注意：密码字段应先进行哈希处理，不应存储明文
            user = User(**user_schema.model_dump())
            
            # 将新用户对象添加到数据库会话
            # self.session.add(user): 将对象标记为"待插入"
            # 实际插入操作在事务提交时执行
            self.session.add(user)
            
            # 返回创建的User对象
            # 注意：此时对象可能尚未持久化到数据库，但已具有数据库分配的ID等属性
            # 如果User模型有自增ID，在返回时通常已填充
            return user
            


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