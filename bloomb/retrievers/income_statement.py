from .base_retriever import BaseRetriever


class IncomeStatementRetriever(BaseRetriever):
    def __init__(self, symbol):
        super(IncomeStatementRetriever, self).__init__(symbol)

    def retrieve(self):
        url_string = "quote/{symbol}/financials?p={symbol}".format(
            symbol=self._symbol)
        html_obj = self._retrieve_resource(url_string)
        return self._parse_html_obj(html_obj)
