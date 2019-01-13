from sqlalchemy import (Boolean, Column, ForeignKey, Integer, Interval, String,
                        Time)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from src.models.kofa.movie import Movie

Base = declarative_base()


class Schedule(Base):
    __tablename__ = 'schedules'
    id = Column(Integer, primary_key=True)
    movie_id = Column(String, ForeignKey('movie.kofa_id'))
    movie = relationship('Movie', back_populates='schedules')
    start_time = Column(Time)
    is_bookable = Column(Boolean)
    is_delivered = Column(Boolean)

    def end_time(self):
        return self.start_time + self.movie.runtime
