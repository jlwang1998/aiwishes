from fastapi import FastAPI, Path, Query
from typing import Annotated

from openai import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# path传参
@app.get("/p/{article_id}")
# async def article_detail(article_id: Annotated[int, Path(ge=2)]):
async def article_detail(
        article_id: int=Path(ge=2)
):
    return {"article_id": article_id}

# 查询传参
@app.get('/article/list')
async def article_list(
        page: Annotated[int, Query(ge=1)]=1,
        size: Annotated[int, Query(ge=10)]=10
):
    return {"page": page, "size": size}

# Body传参
from pydantic import Field
class LoginIn(BaseModel):
    # Field的第一个参数：...，代表该参数不能被省略，不能为空
    email: Annotated[str, Field(..., description="邮箱")]
    password: Annotated[str, Field(..., min_length=6, max_length=20, description="密码")]

@app.post("/login")
async def login(data: LoginIn):
    email = data.email
    password = data.password
    return {"email": email, "password": password}


# 依赖注入
from fastapi import Depends
from typing import Dict

async def page_common(page: int=0, size: int=10):
    return {"page": page, "size": size}

@app.get("/user/list")
async def get_user_list(page_params: Dict=Depends(page_common)):
    page = page_params.get('page')
    size = page_params.get('size')
    return {"page": page, "size": size}

@app.get("/movie/list")
async def get_movie_list(page_params: Dict=Depends(page_common)):
    page = page_params.get('page')
    size = page_params.get('size')
    return {"page": page, "size": size}