from fastapi import APIRouter

from controller.get_card_controller import GetCardController


router = APIRouter()

@router.get("/card")
def get_daily_card():
    file = GetCardController().run({})
    return file
