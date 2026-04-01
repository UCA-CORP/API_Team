from pydantic import BaseModel, Field
from typing import Optional


class Action(BaseModel):
    timestamp: float
    type: str
    shape: int
    position: Optional[str] = None
    position_depart: Optional[str] = None
    position_arrivee: Optional[str] = None


class Statistiques(BaseModel):
    shape_0: int = Field(alias="Shape(0)")
    shape_1: int = Field(alias="Shape(1)")
    shape_2: int = Field(alias="Shape(2)")
    shape_3: int = Field(alias="Shape(3)")
    shape_4: int = Field(alias="Shape(4)")
    shape_5: int = Field(alias="Shape(5)")
    shape_6: int = Field(alias="Shape(6)")
    sum: int = Field(alias="Sum")
    score_ratio: int = Field(alias="Score_ration")  # typo conservée telle quelle dans la DB
    efficiency: int = Field(alias="Efficiency")

    model_config = {"populate_by_name": True}

class Tour(BaseModel):
    Tour: int
    Level: int
    Score: int
    Full_lines: int
    Statistiques: Statistiques
    Actions: list[Action]


class Partie(BaseModel):
    Partie: int
    utilisateur: str
    score_final: int
    temps_jeu: int
    Tours: list[Tour]