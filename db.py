from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib.parse

from dotenv import load_dotenv
load_dotenv()                 

import os 

username = os.environ.get('mongo_username')
passw = os.environ.get('mongo_password')

print(username,passw)

username = urllib.parse.quote_plus(str(username))
passw = urllib.parse.quote_plus(str(passw))

uri = f"mongodb+srv://{username}:{passw}@cluster0.wvqfpmi.mongodb.net/?retryWrites=true&w=majority"
print(uri)
client = MongoClient(uri, server_api=ServerApi('1'))
print('\nhereeeeeee')
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e.args)