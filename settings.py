import json
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('BOT_TOKEN')
CUSTOM_LAUNCH = os.getenv('CUSTOM_LAUNCH')

if CUSTOM_LAUNCH:
    cl=json.loads(CUSTOM_LAUNCH)
else:
    cl ={}