from sqlalchemy import Column, TEXT, INT, BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Test(Base):
    __tablename__ = "data"

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    date = Column(TEXT, nullable=False)
    value = Column(TEXT, nullable=False)