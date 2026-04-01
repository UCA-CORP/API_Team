from fastapi import FastAPI
from .routers import parties
from .routers import tours
from .routers import actions

app = FastAPI(title="API Tetris")

@app.get("/")
def root():
    return {"message": "API Tetris OK"}

app.include_router(parties.router)
app.include_router(tours.router)
app.include_router(actions.router)


