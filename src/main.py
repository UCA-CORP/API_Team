from fastapi import FastAPI

from src.routers import analytics
from .routers import parties
from .routers import tours
from .routers import actions
from .routers import statistiques

app = FastAPI(title="API Tetris")

@app.get("/")
def root():
    return {"message": "API Tetris OK"}

app.include_router(parties.router)
app.include_router(tours.router)
app.include_router(actions.router)
app.include_router(statistiques.router)
app.include_router(analytics.router)

