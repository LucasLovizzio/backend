from pymongo import MongoClient

#Base de datos local
#db_client = MongoClient().local      # Si no ponemos nada en los parametros se conecta a localhost

#Base de datos remota

db_client = MongoClient(
    "mongodb+srv://test:test@cluster0.nbjmyvj.mongodb.net/?retryWrites=true&w=majority").test