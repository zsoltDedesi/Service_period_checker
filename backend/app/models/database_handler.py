from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base


class DataBaseHandler:
    def __init__(self, database_url):
        # Create SQLAlchemy Engine
        self.__engine = create_engine(database_url, echo=True)

        # Create Session
        self.__session_local = sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False
        )

    @property
    def engine(self):
        return self.__engine

    def session(self):
        return self.__session_local()

    def init_db(self):
        with self.__engine.begin() as conn:
            Base.metadata.create_all(conn)
        print("DB has been initialized!")
