from .balance_sheet import BalanceSheetRetriever
from .cash_flow import CashFlowRetriever
from .income_statement import IncomeStatementRetriever


class StockDataRetriever(object):
    def __init__(self, symbol):
        self._symbol = symbol

    def retrieve(self):
        result = list()
        bsr_obj = BalanceSheetRetriever(self._symbol).retrieve()
        cfr_obj = CashFlowRetriever(self._symbol).retrieve()
        isr_obj = IncomeStatementRetriever(self._symbol).retrieve()
        bsr_obj.reverse()
        cfr_obj.reverse()
        isr_obj.reverse()
        list_dates = bsr_obj.pop()
        cfr_obj.pop()
        isr_obj.pop()
        bsr_obj.reverse()
        cfr_obj.reverse()
        isr_obj.reverse()
        result = list_dates + isr_obj + bsr_obj + cfr_obj
        return result
