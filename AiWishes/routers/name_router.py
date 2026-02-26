from fastapi import APIRouter, Depends
from schemas.name_schemas import NameIn, NameOut
from core.agent import generate_names
from core.auth import AuthHandler

router = APIRouter(prefix="/name")
auth_handler = AuthHandler()

@router.post("/", response_model=NameOut)
async def take_names(
    data: NameIn,
    user_id: int=Depends(auth_handler.auth_access_dependency)
):
    name_result = await generate_names(data)
    return NameOut(names=name_result.names)