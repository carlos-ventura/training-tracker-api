from contextlib import asynccontextmanager
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware


from app.auth import validate_api_key
from fastapi import APIRouter, Depends, FastAPI, HTTPException, Response
from sqlalchemy.orm import Session

from app.constants import DESCRIPTION
from app.db.setup import Base, engine, session
from app.enums import TrainingGame, TrainingType
from app.models import Training
from app.tasks import (
    delete_training_task,
    load_all_training_task,
    load_trainings_game_task,
    load_trainings_type_task,
    save_training_task,
)

load_dotenv()

def get_db_session():
    db_session = session()
    try:
        yield db_session
    finally:
        db_session.close()


@asynccontextmanager
async def lifespan(app: FastAPI):
    conn = engine.connect()
    try:
        Base.metadata.create_all(bind=engine)
        yield
    finally:
        conn.close()


app = FastAPI(
    title="Training Tracker",
    description=DESCRIPTION,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

public_router = APIRouter()
private_router = APIRouter(dependencies=[Depends(validate_api_key)])

@public_router.post("/login", dependencies=[])
async def login(api_key:str, response: Response):
    if api_key != os.getenv("API_KEY"):
         raise HTTPException(status_code=401, detail="Unauthorized")

    response.set_cookie(
        key="api_key", 
        value=api_key, 
        httponly=True, 
        expires=(datetime.now(tz=timezone.utc) + timedelta(days=30)),
        secure=True,
        samesite="Strict"
    )
    
    return {"message": "Logged in successfully"}

@private_router.post("/logout")
async def logout(response: Response):
    response.delete_cookie("api_key")
    
    return {"message": "Logged out successfully"}


@private_router.get("/trainings/")
def load_trainings(db_session: Session = Depends(get_db_session)):
    return load_all_training_task(db_session)


@private_router.get("/trainings/game")
def load_training_game(game: TrainingGame, db_session: Session = Depends(get_db_session)):
    return load_trainings_game_task(game, db_session)


@private_router.get("/training/type")
def load_training_type(training_type: TrainingType, db_session: Session = Depends(get_db_session)):
    return load_trainings_type_task(training_type, db_session)


@private_router.post("/trainings/")
def save_training(training: Training, db_session: Session = Depends(get_db_session)):
    save_training_task(training, db_session)


@private_router.delete("/trainings/{training_id}")
def delete_training(training_id: str, db_session: Session = Depends(get_db_session)):
    delete_training_task(training_id, db_session)

app.include_router(public_router)
app.include_router(private_router)