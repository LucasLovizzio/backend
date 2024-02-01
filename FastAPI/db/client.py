from pymongo import MongoClient

db_client = MongoClient().local      # Si no ponemos nada en los parametros se conecta a localhost
