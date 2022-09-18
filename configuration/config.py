from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.environ.get("TOKEN")

TECHNOPARK = 'Technopark'
CREDITASIA = 'CreditAsia'
HISTORY = 'View History'

GREETING_MESSAGE = 'Hello, I am Price Bot, where do I search?'
NOTFOUND_MESSAGE = 'Unfortunately, I did not find anything'
QUERY_MESSAGE = 'What are you searching for?'
UNKNOWNCOMMAND_MESSAGE = 'I do not understand this command'