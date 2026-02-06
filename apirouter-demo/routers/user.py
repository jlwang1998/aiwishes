from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])


# /user/list
@router.get("/list")
async def user_list():
    return {"users": ['张三', '李四']}


# /user/123
@router.get('/{user_id}')
async def user_detail(user_id: int):
    return {"user_id": user_id}