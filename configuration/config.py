from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.environ.get("TOKEN")

TECHNOPARK = 'Technopark'
CREDITASIA = 'CreditAsia'
HISTORY = 'View History'
COMPARE = 'Compare prices'

GREETING_MESSAGE = 'Hello, I am Price Bot, where do I search?'
NOTFOUND_MESSAGE = 'Unfortunately, I did not find anything'
QUERY_MESSAGE = 'What are you searching for?'
UNKNOWNCOMMAND_MESSAGE = 'I do not understand this command'
ASKAGAIN_MESSAGE = 'Anything else I can do for you?'

USER_NOTFOUND = 'User not found, anything else I can do for you?'

LOAD_TIMEOUT = 2

DATABASE_CONNECTION = 'postgresql+psycopg2://mlfhuntr:@localhost:6543/telebot'