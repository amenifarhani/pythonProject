from sqlalchemy import Integer, Column, DateTime, String
from datetime import datetime

from cleanupservice import Base


class Training(Base):
    __tablename__ = 'trainings'
    __table_args__ = {'extend_existing': True}  # Ajouter cette ligne

    training_id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    domain = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    likes_count = Column(Integer)
    approved = Column(Integer)

