import os
from dotenv import load_dotenv

load_dotenv()

# API_TOKEN = os.environ['API_TOKEN']
API_TOKEN = os.getenv('API_TOKEN')
BASE_URL = 'http://api.weatherapi.com/v1'
