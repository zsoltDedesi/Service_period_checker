import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class EnvData:
    DATABASE_URL = os.getenv("DATABASE_URL", 
                            f"postgresql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}"
                            f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")


# class Config:
#     SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/dbname'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SECRET_KEY = 'your_secret_key'


# class DevelopmentConfig(Config):
#     DEBUG = True
