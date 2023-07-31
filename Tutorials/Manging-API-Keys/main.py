import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("SECRET_API_KEY")

print(api_key)