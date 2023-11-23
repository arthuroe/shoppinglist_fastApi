from typing import Optional

from pydantic import BaseModel


class ShoppingList(BaseModel):
    """
    Shopping list model
    """
    name: str
    is_active: bool
    items: Optional[dict]
