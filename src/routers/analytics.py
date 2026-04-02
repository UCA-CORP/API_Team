from fastapi import APIRouter, HTTPException
from src.crud_functions import *
from src.database.raw_data.models_raw_data import (
    KPIGlobauxResponse,
    UserLevelPoint,
    LevelCountPoint,
    ScoreFinalEvolutionPoint,
    ScoreTourEvolutionPoint
)


router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/kpis/globaux", response_model=KPIGlobauxResponse)
async def lire_kpi_globaux():
    return get_kpi_globaux()


@router.get("/repartition/users-level", response_model=list[UserLevelPoint])
async def lire_users_level():
    return get_users_level_points()



@router.get("/evolution/score-final", response_model=list[ScoreFinalEvolutionPoint])
async def lire_evolution_score_final(utilisateur: str, partie: int ):
    return get_score_final_evolution(utilisateur=utilisateur, partie=partie)


@router.get("/evolution/performance", response_model=list[ScoreTourEvolutionPoint])
async def lire_evolution_performance(utilisateur: str, partie: int ):
    return get_score_tour_evolution(partie=partie, utilisateur=utilisateur)