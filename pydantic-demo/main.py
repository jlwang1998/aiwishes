from pydantic import BaseModel, ValidationError
from datetime import date
from typing import Optional, List


class User(BaseModel):
    id: int
    name: str
    # date|None = Optional[date]
    date_joined: Optional[date]
    departments: List[str]

try:
    user = User(id="ab", name="张三", date_joined=date(year=2030, month=10, day=1), departments=['技术部', "产品部"])
    print(user.model_dump())
except ValidationError as e:
    print(e.errors())