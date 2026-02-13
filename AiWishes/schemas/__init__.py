"""在视图函数中，在某些操作，不需要返回具体数据时，我们可以返回一个固定的响应格式。"""

from pydantic import BaseModel, Field
from typing import Annotated, Literal

class ResponseOut(BaseModel):
    # - Literal["success", "failure"]：表示result字段只能接受字符串"success"或"failure"这两个值，其他值会引发验证错误
    # - Field("success", description="操作结果")：为字段添加Pydantic的Field配置
    #   - "success"：第一个位置参数，设置字段的默认值为"success"。如果不提供result值，将自动使用此默认值
    result: Annotated[Literal["success", "failure"], Field("success", description="操作结果")]