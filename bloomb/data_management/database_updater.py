import pymongo
from ..conf.settings import conf_obj


class DatabaseUpdater(object):
    def __init__(self, symbol, object_creator):
        self._symbol = symbol
        self._object_creator = object_creator

    def update(self):
        self._setup()
        result = dict(status=None, msg=None)
        for dt, record in self._object_creator.iteritems():
            if self._is_new_data(dt):
                record.update({"date": dt})
                self.db[self._symbol].insert(record)
        result["status"] = "ok"
        result["msg"] = None
        return result

    def _is_new_data(self, dt):
        res = self.db[self._symbol].find_one({"date": dt})
        return res is None

    def _store_in_db(self):
        pass

    def _setup(self):
        host = conf_obj.get("db_credentials", "host")
        port = conf_obj.get("db_credentials", "port")
        db_name = conf_obj.get("db_credentials", "db_name")
        mongo_uri = "mongodb://{host}:{port}/{db_name}".\
            format(host=host, port=port, db_name=db_name)
        client = pymongo.MongoClient(mongo_uri)
        self.db = client.get_default_database()
