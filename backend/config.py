import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "gemma2-9b-it"

DATABASE_URL = "sqlite:///./crm.db"