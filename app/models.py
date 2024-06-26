from datetime import date as date_datetime

from pydantic import BaseModel, Field

from app.enums import TrainingGame, TrainingSubType, TrainingType


class Training(BaseModel):
    game: TrainingGame = Field(examples=[TrainingGame.RocketLeague])
    type: TrainingType = Field(examples=[TrainingType.AirRoll])
    sub_type: TrainingSubType = Field(examples=[TrainingSubType.TornadoSping])
    minutes: float
    date: date_datetime = date_datetime.today()
