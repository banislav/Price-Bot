from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.environ.get("TOKEN")

TECHNOPARK = 'Technopark'
CREDITASIA = 'CreditAsia'
HISTORY = 'View History'

GREETING_MESSAGE = 'Hello, I am price bot, what do you want to do?'
NOTFOUND_MESSAGE = 'Unfortunately, I can not understand you'
QUERY_MESSAGE = 'What are you searching for?'