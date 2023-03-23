import pymongo
from APS_sensor.constant.database import DATABASE_NAME
from APS_sensor.constant.env_variable import MONGODB_URL_KEY
from APS_sensor.logger import logging
import certifi
import os
ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:

            if MongoDBClient.client is None:
                #mongo_db_url = os.getenv(MONGODB_URL_KEY)
                mongo_db_url="mongodb+srv://mukeshbabu447:Mukeshbabu@cluster0.ebx4e8b.mongodb.net/?retryWrites=true&w=majority"
                print(mongo_db_url)
                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url) 
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info(f"Connected to {self.database_name} Database")

        except Exception as e:
            raise e