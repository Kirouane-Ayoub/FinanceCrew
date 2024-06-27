import utils.settings as settings
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

load_dotenv()
gemini = ChatGoogleGenerativeAI(model=settings.DEFAULT_GEMINI)

groq = ChatGroq(model=settings.DEFAULT_GROQ)

command = ChatCohere(model=settings.DEFAULT_COHERE)
