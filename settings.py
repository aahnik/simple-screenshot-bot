import json
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')

WIDTH = int(os.getenv('WIDTH','1920'))
HEIGHT = int(os.getenv('HEIGHT', '1080'))
