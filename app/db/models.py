from sqlalchemy import Column, Date, Float, String

from app.db.setup import Base


class TrainingModel(Base):
    __tablename__ = "training"

    id = Column(String, primary_key=True)
    game = Column(String, nullable=False)
    type = Column(String, nullable=False)
    sub_type = Column(String, nullable=False)
    hours = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
