from fastapi import FastAPI

app = FastAPI()


# 服务器在定义URL的时候，用了什么method，那么客户端在请求这个URL的时候就要用相同的method
# GET：从服务器上获取资源的
# POST：提交数据到服务器
# DELETE：要删除服务器上的数据
# PUT：要修改服务器上的数据
@app.get("/")
async def root():
    # 异步函数、协程
    # await 访问数据库()
    return {"message": "Hello World"}

# /hello/a
# /hello/b
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
