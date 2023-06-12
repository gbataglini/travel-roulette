import os 
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('DATABASE_HOST')
USER = os.getenv('DATABASE_USER')
PASSWORD = os.getenv('DATABASE_PASSWORD')