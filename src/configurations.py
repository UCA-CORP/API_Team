
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://nakavouavinypresty_db_user:NRl5dIC5jIyLhEAQ@cluster0.acr2qev.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.tint_db 
collection = db["tint_raw_data"]