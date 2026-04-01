from fastapi import APIRouter, HTTPException, status
from src.database.models import Action
from src.crud_functions import *

router = APIRouter(
    prefix="/parties/{Partie}/tours/{Tour}/actions",
    tags=["actions"]
)


@router.get("/", response_model=list[Action])
async def lire_actions(Partie: int, Tour: int):
    tour = get_tour_by_id(Partie, Tour)
    return tour.get("Actions", [])

