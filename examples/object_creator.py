import pprint
from bloomb.parsers.object_creator import ObjectCreator
from bloomb.retrievers.stock_data_retriever import StockDataRetriever

data_retrieved = StockDataRetriever("XOM").retrieve()
pprint.pprint(ObjectCreator(data_retrieved).create())
