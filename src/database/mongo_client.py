from motor.motor_asyncio import AsyncIOMotorClient


MONGO_URL = "mongodb://mongo:27017"
DATABASE_NAME = "transflow"
COLLECTION_NAME = "corridas"

client = AsyncIOMotorClient(MONGO_URL)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

def get_collection():
    return collection