from abc import ABCMeta, abstractmethod
import requests
from bs4 import BeautifulSoup
from ..conf.settings import conf_obj
from ..helpers.data_type_conversions import text_to_float, text_to_date


class BaseRetriever(object):
    __metaclass__ = ABCMeta

    def __init__(self, symbol):
        self._symbol = symbol

    @abstractmethod
    def retrieve(self):
        pass

    def _parse_html_obj(self, html_obj):
        result = list()
        income_statement_rows = html_obj.find_all(
            attrs={"class": "Bdbw(1px) Bdbc($lightGray) Bdbs(s) H(36px)"})
        result.append(self._get_list_dates(income_statement_rows[0]))
        for row in income_statement_rows[1:]:
            row_data = list()
            categ_el = row.find(attrs={"class": "Fz(s) H(35px) Va(m)"})
            if categ_el:
                cat_name = categ_el.span.text
                row_data.append(cat_name)
                elements = row.find_all(attrs={"class": "Fz(s) Ta(end)"})
                for el in elements:
                    cat_value_els_green = el.find_all(
                        attrs={"class": "Trsdu(0.3s) C($dataGreen)"})
                    cat_value_els_red = el.find_all(
                        attrs={"class": "Trsdu(0.3s) C($dataRed)"})
                    all_cat_els = cat_value_els_green + cat_value_els_red
                    if all_cat_els == []:
                        row_data.append(None)
                    for value_el in all_cat_els:
                        row_data.append(text_to_float(value_el.span.text))
            if len(row_data) < 3:
                continue
            result.append(row_data)
        summary_elements = html_obj.find_all(
            attrs={"class": "Bdbw(1px) Bdbc($lightGray) Bdbs(s) H(36px)"})
        for summary_row in summary_elements:
            row_data = list()
            categ_el = summary_row.find(attrs={"class": "Fw(b) Py(8px) Pt(36px)"})
            if categ_el:
                cat_name = categ_el.span.text
                row_data.append(cat_name)
                elements = summary_row.find_all(
                    attrs={"class": "Fw(b) Ta(end) Py(8px) Pt(36px)"})
                for el in elements:
                    cat_value_els_green = el.find_all(
                        attrs={"class": "Trsdu(0.3s) C($dataGreen)"})
                    cat_value_els_red = el.find_all(
                        attrs={"class": "Trsdu(0.3s) C($dataRed)"})
                    all_cat_els = cat_value_els_green + cat_value_els_red
                    if all_cat_els == []:
                        row_data.append(None)
                    for value_el in all_cat_els:
                        row_data.append(text_to_float(value_el.span.text))
            if len(row_data) < 3:
                continue
            result.append(row_data)
        summary_other_elements = html_obj.find_all(
            attrs={"class": "Bdbw(0px)! H(36px)"})

        for summary_other_row in summary_other_elements:
            row_data = list()
            categ_el = summary_other_row.find(attrs={"class": "Fw(b) Fz(s) Pb(20px)"})
            if categ_el:
                cat_name = categ_el.span.text
                row_data.append(cat_name)
                elements = summary_other_row.find_all(
                    attrs={"class": "Fw(b) Fz(s) Ta(end) Pb(20px)"})
                for el in elements:
                    cat_value_els_green = el.find_all(
                        attrs={"class": "Trsdu(0.3s) C($dataGreen)"})
                    cat_value_els_red = el.find_all(
                        attrs={"class": "Trsdu(0.3s) C($dataRed)"})
                    all_cat_els = cat_value_els_green + cat_value_els_red
                    if all_cat_els == []:
                        row_data.append(None)
                    for value_el in all_cat_els:
                        row_data.append(text_to_float(value_el.span.text))
            if len(row_data) < 3:
                continue
            result.append(row_data)
        return result

    def _get_list_dates(self, data_obj):
        list_date_obj = data_obj.find_all(
            attrs={"class": "C($gray) Ta(end)"})
        return [text_to_date(do.span.text, "%m/%d/%Y") for do in list_date_obj]

    def _get_base_url(self):
        return conf_obj.get("yahoo_api", "base_url")

    def _retrieve_resource(self, url_string):
        url = "https://{base_url}/{url_string}".format(
            base_url=self._get_base_url(), url_string=url_string)
        body = requests.get(url=url).content
        return BeautifulSoup(body, 'html.parser')
