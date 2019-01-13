from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base


class TelegramBase(object):
    telegram_id = Column(Integer, primary_key=True)


TelegramBase = declarative_base(TelegramBase)
