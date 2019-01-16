from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import (Boolean, Column, ForeignKey, Integer, Interval, String,
                        Time)


Base = declarative_base()


class KofaBase(Base):
    __abstract__ = True
    kofa_id = Column(String, primary_key=True)


class TelegramBase(Base):
    __abstract__ = True
    telegram_id = Column(Integer, primary_key=True)


class Movie(KofaBase):
    __tablename__ = 'movie'
    title = Column(String)
    director = Column(String)
    synopsis = Column(String)
    url = Column(String)
    runtime = Column(Interval(native=True))
    schedules = relationship('Schedule', back_populates='movie')


class Schedule(Base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True)
    movie_kofa_id = Column(String, ForeignKey('movie.kofa_id'))
    movie = relationship('Movie', back_populates='schedules')
    start_time = Column(Time)
    is_bookable = Column(Boolean)
    is_delivered = Column(Boolean)

    def end_time(self):
        return self.start_time + self.movie.runtime


class Chat(TelegramBase):
    __tablename__ = 'chat'
