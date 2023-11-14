from typing import List

from fastapi import APIRouter

from api.shoppinglist.shoppinglist_model import ShoppingList


router = APIRouter()
shoppinglists = []


@router.get("/shoppinglists", response_model=List[ShoppingList])
async def get_shoppinglists() -> List[ShoppingList]:
    """
    Return shopping lists
    """
    return shoppinglists


@router.get("/shoppinglists/{id}", response_model=List[ShoppingList])
async def get_shoppinglist(id: int) -> List[ShoppingList]:
    """
    Return shopping list
    """
    if not shoppinglists:
        return []

    return shoppinglists[id]


@router.post("/shoppinglists", response_model=List[ShoppingList])
async def create_shoppinglist(shoppinglist: ShoppingList) -> List[ShoppingList]:
    """
    Create shopping lists
    """
    shoppinglists.append(shoppinglist)
    return shoppinglists


@router.put("/shoppinglists", response_model=List[ShoppingList])
async def update_shoppinglist(shoppinglist: ShoppingList) -> List[ShoppingList]:
    """
    Create shopping lists
    """
    shoppinglists.append(shoppinglist)
    return shoppinglists
