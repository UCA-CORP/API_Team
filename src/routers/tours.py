from fastapi import APIRouter, HTTPException, status
from ..database.models import Tour
from src.crud_functions import *

router = APIRouter(
    prefix="/parties/{partie_id}/tours",
    tags=["tours"]
)

@router.get("/", response_model=list[Tour])
async def lire_tours(partie_id: int):
    partie = get_partie_by_id(partie_id)
    return get_tours_by_partie_id(partie_id)


@router.get("/{tour_id}", response_model=Tour)
async def lire_tour(partie_id: int, tour_id: int):
    partie = get_partie_by_id(partie_id)
    tour = get_tour_by_id(partie_id, tour_id)
    return tour

