from bloomb.retrievers.stock_data_retriever import StockDataRetriever
from bloomb.parsers.object_creator import ObjectCreator
from bloomb.data_management.database_updater import DatabaseUpdater

SYMBOL = "DOW"
data_retrieved = StockDataRetriever(SYMBOL).retrieve()
object_created = ObjectCreator(data_retrieved).create()
DatabaseUpdater(SYMBOL, object_created).update()
