import pymongo
from ..conf.settings import conf_obj


def retrieve_financial_data(symbol):
    host = conf_obj.get("db_credentials", "host")
    port = conf_obj.get("db_credentials", "port")
    db_name = conf_obj.get("db_credentials", "db_name")
    mongo_uri = "mongodb://{host}:{port}/{db_name}".\
        format(host=host, port=port, db_name=db_name)
    client = pymongo.MongoClient(mongo_uri)
    db = client.get_default_database()
    return db[symbol].find().sort([("date", pymongo.DESCENDING)])
