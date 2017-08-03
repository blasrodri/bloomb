from potion_client import Client
from ..conf.settings import conf_obj


def company_id_to_symbol(company_id):
    host = conf_obj.get("information_system", "host")
    port = conf_obj.get("information_system", "port")
    information_system_url = "http://{host}:{port}".format(
        host=host, port=port)
    client = Client(information_system_url)
    symbol = client.Company.fetch(id=company_id).symbol
    return symbol


def get_companies_info():
    host = conf_obj.get("information_system", "host")
    port = conf_obj.get("information_system", "port")
    information_system_url = "http://{host}:{port}".format(
        host=host, port=port)
    client = Client(information_system_url)
    return dict((str(x.id), x.symbol) for x in client.Company.instances())
