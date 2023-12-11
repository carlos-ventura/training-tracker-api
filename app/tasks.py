from sqlalchemy.orm import Session

from app.db.dals.training_dal import TrainingDAL
from app.db.models import TrainingModel
from app.enums import TrainingGame, TrainingType
from app.models import Training


def save_training_task(training: Training, db_session: Session):
    training_dal = TrainingDAL(db_session)
    training_dal.save(training)

    return {"message": "Training inserted successfully"}


def load_all_training_task(db_session: Session) -> list[TrainingModel]:
    training_dal = TrainingDAL(db_session)
    return training_dal.get_all()


def load_trainings_game_task(game: TrainingGame, db_session: Session) -> dict:
    training_dal = TrainingDAL(db_session)
    return training_dal.get_game(game)


def load_trainings_type_task(training_type: TrainingType, db_session: Session) -> dict:
    training_dal = TrainingDAL(db_session)
    return training_dal.get_type(training_type)


def delete_training_task(training_id: str, db_session: Session) -> dict:
    training_dal = TrainingDAL(db_session)
    training_dal.delete(training_id)

    return {"message": f"Training deleted successfully: {training_id}"}
