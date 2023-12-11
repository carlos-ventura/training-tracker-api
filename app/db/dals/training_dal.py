import uuid

from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.db.dals.training_utils import process_game_query, process_type_query
from app.db.models import TrainingModel
from app.enums import TrainingGame, TrainingType
from app.models import Training


class TrainingDAL():
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def save(self, training: Training) -> None:
        training_model = TrainingModel(**training.model_dump())
        training_model.id = str(uuid.uuid4())

        self.db_session.add(training_model)
        self.db_session.commit()

    def get(self, training_id: str) -> TrainingModel | None:
        return self.db_session.query(TrainingModel).get(training_id)

    def get_all(self) -> list[TrainingModel]:
        return self.db_session.query(TrainingModel).all()

    def get_game(self, game: TrainingGame) -> dict:
        query = self.db_session.query(
            TrainingModel.game,
            TrainingModel.type,
            TrainingModel.sub_type,
            func.count().label("count"),
            func.sum(TrainingModel.hours).label("hours")
        ).group_by(
            TrainingModel.game,
            TrainingModel.type,
            TrainingModel.sub_type
        ).filter(
            TrainingModel.game == game
        )

        return process_game_query(query)

    def get_type(self, training_type: TrainingType):
        query = self.db_session.query(
            TrainingModel.game,
            TrainingModel.type,
            func.count().label("count"),
            func.sum(TrainingModel.hours).label("hours")
        ).group_by(
            TrainingModel.game,
            TrainingModel.type,
        ).filter(
            TrainingModel.type == training_type
        )

        return process_type_query(query)

    def delete(self, training_id: str) -> None:
        if training := self.get(training_id):
            self.db_session.delete(training)
            self.db_session.commit()
        else:
            raise HTTPException(status_code=404, detail="Training not found")
