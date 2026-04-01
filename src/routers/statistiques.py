from fastapi import APIRouter, HTTPException, status
from src.database.models import Statistiques
from src.crud_functions import *

router = APIRouter(
    prefix="/parties/{Partie}/tours/{Tour}/statistiques",
    tags=["statistiques"]
)


@router.get("/", response_model=Statistiques)
async def lire_statistiques(Partie: int, Tour: int):
    tour = get_tour_by_id(Partie, Tour)    
    return tour.get("Statistiques", [])

