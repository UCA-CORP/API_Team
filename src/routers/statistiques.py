from fastapi import APIRouter, HTTPException, status
from src.database.models import Statistiques
from src.crud_functions import *

router = APIRouter(
    prefix="/parties/{partie_id}/tours/{tour_id}/statistiques",
    tags=["statistiques"]
)


@router.get("/", response_model=Statistiques)
async def lire_statistiques(partie_id: int, tour_id: int):
    partie = get_partie_by_id(partie_id)
    tour = get_tour_by_id(partie_id, tour_id)    
    return tour.get("statistiques", [])

