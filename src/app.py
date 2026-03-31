from fastapi import FastAPI, HTTPException, Depends
from contextlib import asynccontextmanager
# from typing import Annotated

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from sqlmodel import Session, select
from database import create_db_and_tables, Chat, engine

from pydantic import BaseModel


from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    

app = FastAPI(lifespan=lifespan)


@app.post("/chats/")
def create_chat(chat: Chat):
    with Session(engine) as session:
        session.add(chat)
        session.commit()
        session.refresh(chat)
        return chat
    
@app.get("/chats/") 
def get_chats():
    with Session(engine) as session:
        cats = session.exec(select(Chat)).all()
        return cats
    
@app.delete("/chats/{chat_id}")
def delete_chat_by_id(chat_id: int):
    with Session(engine) as session:
        chat = session.get(Chat, chat_id)
        if not chat:
            raise HTTPException(status_code=404, detail="Cat not found")
        
        session.delete(chat)
        session.commit()
        return {"ok": True}
    