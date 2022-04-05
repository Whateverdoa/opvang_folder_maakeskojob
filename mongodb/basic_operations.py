import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient

# load config from a .env file:
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)

# list all the databases in the cluster:
for db_info in client.list_databases_names():
    print(db_info)