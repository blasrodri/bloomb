import datetime


def to_nominal_unit(f):
    def inner(txt_el):
        return f(txt_el) * 1000
    return inner


@to_nominal_unit
def text_to_float(text_element):
    return float(text_element.replace(",", ""))


def text_to_date(text_element, fmt=None):
    return datetime.datetime.strptime(text_element, fmt)
