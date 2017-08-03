from flask import Flask, jsonify
from flask_cors import CORS
import json
from bson import json_util
from ..data_management.database_retriever import retrieve_financial_data
from ..helpers.mappers import get_companies_info
from ..retrievers.stock_data_retriever import StockDataRetriever
from ..parsers.object_creator import ObjectCreator
from ..data_management.database_updater import DatabaseUpdater
from potion_client import Client
from ..conf.settings import conf_obj
app = Flask(__name__)
CORS(app)


@app.route("/get_financial_data/<company_id>")
def hello(company_id):
    symbol = company_id_symbol_map.__getitem__(company_id)
    v = retrieve_financial_data(symbol)
    fin_data_list = [json.loads(json_util.dumps(x)) for x in v]
    json_res = jsonify({"symbol": symbol, "data": fin_data_list})
    return json_res


@app.route("/update_financial_data/<symbol>", methods=["GET"])
def update_financial_data(symbol):
    result = dict(status=None, msg=None, data=list())
    try:
        data_retrieved = StockDataRetriever(symbol).retrieve()
        object_created = ObjectCreator(data_retrieved).create()
        DatabaseUpdater(symbol, object_created).update()
    except Exception, e:
        result["status"] = "err"
        result["msg"] = str(e)
    else:
        result["status"] = "ok"
        result["data"].append(symbol)
    return jsonify(result)
