"""Friendly message functions"""

from fastapi import APIRouter

router = APIRouter()


@router.get('/hello_message')
async def hello_greeting(name="Andrew"):
    """Returns a friendly greeting to you!"""
    # you want to return dictionaries in FastAPI
    return {"greeting": f"Hello, {name}!"}