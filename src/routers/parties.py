from fastapi import APIRouter, HTTPException
from src.crud_functions import *
from src.database.raw_data.models_raw_data import Partie

router = APIRouter(prefix="/parties", tags=["parties"])

@router.get("/", response_model=list[Partie])
async def lire_parties():
    return get_all_parties()

@router.get("/{Partie}", response_model=Partie)
async def lire_partie(Partie: int):
    partie = get_partie_by_id(Partie)
    return partie