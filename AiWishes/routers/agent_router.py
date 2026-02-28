from fastapi import APIRouter, Depends
from schemas.name_schemas import NameIn, NameOut
from schemas.wish_schemas import WishIn, WishOut
from core.agent import generate_names,generate_wishes
from core.auth import AuthHandler

router = APIRouter(prefix="/agent")
auth_handler = AuthHandler()

@router.post("/name", response_model=NameOut)
async def take_names(
    data: NameIn,
    user_id: int=Depends(auth_handler.auth_access_dependency)
):
    name_result = await generate_names(data)
    return NameOut(names=name_result.names)

@router.post("/wish", response_model=WishOut)
async def take_wishes(
    data: WishIn,
    user_id: int=Depends(auth_handler.auth_access_dependency)
):
    wish_result = await generate_wishes(data)
    return WishOut(wishes=wish_result.wishes)