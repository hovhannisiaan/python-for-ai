import os
from dotenv import load_dotenv

load_dotenv()

# Read from environment
api_key = os.environ.get("API_KEY")
database = os.environ.get("DATABASE_NAME", "default.db")


print(api_key)
