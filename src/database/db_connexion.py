
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#uri = "mongodb+srv://nakavouavinypresty_db_user:NRl5dIC5jIyLhEAQ@cluster0.acr2qev.mongodb.net/?appName=Cluster0"

# en local
uri = "mongodb://localhost:27017"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.tint_db 
collection_tint_raw_data = db["tint_raw_data"]
collection_tint_transformed_data = db["tint_transformed_data"]

try:
    client.admin.command('ping')
    print("✅ Connexion MongoDB réussie")
except Exception as e:
    print(f" Erreur : {e}")