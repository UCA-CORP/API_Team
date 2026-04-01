from fastapi import APIRouter, HTTPException, status
from ..database.models import Tour
from src.crud_functions import *

router = APIRouter(
    prefix="/parties/{Partie}/tours",
    tags=["tours"]
)

@router.get("/", response_model=list[Tour])
async def lire_tours(Partie: int):
    tours = get_tours_by_partie_id(Partie)
    return tours


@router.get("/{Tour}", response_model=Tour)
async def lire_tour(Partie: int, Tour: int):
    tour = get_tour_by_id(Partie, Tour)
    return tour

