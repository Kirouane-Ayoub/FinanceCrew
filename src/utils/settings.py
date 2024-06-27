import os

from dotenv import load_dotenv

load_dotenv()

ALPHAADVANTAGE_APIKEY = os.getenv("ALPHAADVANTAGE_APIKEY")

DEFAULT_COHERE = "command-r-plus"
DEFAULT_GEMINI = "gemini-1.5-flash"
DEFAULT_GROQ = "llama3-70b-8192"
