from datetime import date as date_datetime

from pydantic import BaseModel

from app.enums import TrainingGame, TrainingSubType, TrainingType


class Training(BaseModel):
    game: TrainingGame
    type: TrainingType
    sub_type: TrainingSubType
    hours: float
    date: date_datetime = date_datetime.today()
