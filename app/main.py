from contextlib import asynccontextmanager
from dotenv import load_dotenv

import app.auth

from fastapi import Depends, FastAPI
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
    lifespan=lifespan,
    dependencies=[Depends(app.auth.validate_api_key)]
)


@app.get("/trainings/")
def load_trainings(db_session: Session = Depends(get_db_session)):
    return load_all_training_task(db_session)


@app.get("/trainings/game")
def load_training_game(game: TrainingGame, db_session: Session = Depends(get_db_session)):
    return load_trainings_game_task(game, db_session)


@app.get("/training/type")
def load_training_type(training_type: TrainingType, db_session: Session = Depends(get_db_session)):
    return load_trainings_type_task(training_type, db_session)


@app.post("/trainings/")
def save_training(training: Training, db_session: Session = Depends(get_db_session)):
    save_training_task(training, db_session)


@app.delete("/trainings/{training_id}")
def delete_training(training_id: str, db_session: Session = Depends(get_db_session)):
    delete_training_task(training_id, db_session)
