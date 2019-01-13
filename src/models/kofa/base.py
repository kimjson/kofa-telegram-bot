from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base


class KofaBase(object):
    kofa_id = Column(String, primary_key=True)


KofaBase = declarative_base(KofaBase)
