from fastapi import APIRouter, HTTPException, status
from src.database.models import Action
from src.crud_functions import *

router = APIRouter(
    prefix="/parties/{partie_id}/tours/{tour_id}/actions",
    tags=["actions"]
)


@router.get("/", response_model=Action)
async def lire_actions(partie_id: int, tour_id: int):
    partie = get_partie_by_id(partie_id)
    tour = get_tour_by_id(partie_id, tour_id)
    return tour.get("actions", [])

