from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import pandas as pd

Base = declarative_base()

class Training(Base):
    __tablename__ = 'trainings'

    training_id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    domain = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    likes_count = Column(Integer)
    approved = Column(Integer)

def delete_expired_trainings_and_save_to_excel(database_url):
    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        current_time = datetime.now()
        expired_trainings = session.query(Training).filter(Training.end_date < current_time).all()

        if expired_trainings:
            expired_trainings_data = [
                {
                    "trainingId": training.training_id,
                    "title": training.title,
                    "description": training.description,
                    "domain": training.domain,
                    "startDate": training.start_date.strftime('%Y-%m-%d %H:%M:%S'),  # Format the date here
                    "endDate": training.end_date.strftime('%Y-%m-%d %H:%M:%S'),  # Format the date here
                    "likesCount": training.likes_count,
                    "approved": training.approved
                }
                for training in expired_trainings
            ]
            df = pd.DataFrame(expired_trainings_data)
            df.to_excel("expired_trainings.xlsx", index=False)

            for training in expired_trainings:
                session.delete(training)

            session.commit()
            print(f"Deleted {len(expired_trainings)} expired trainings and saved them to 'expired_trainings.xlsx'.")
        else:
            print("No expired trainings found.")

    except Exception as e:
        session.rollback()
        print(f"An error occurred: {e}")
        raise
    finally:
        session.close()
