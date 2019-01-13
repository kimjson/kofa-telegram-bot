from sqlalchemy import Column, String, Interval
from sqlalchemy.orm import relationship

from src.models.kofa.base import KofaBase


class Movie(KofaBase):
    __tablename__ = 'movies'
    title = Column(String)
    director = Column(String)
    synopsis = Column(String)
    url = Column(String)
    runtime = Column(Interval(native=True))
    schedules = relationship('Schedule', back_populates='movie')
