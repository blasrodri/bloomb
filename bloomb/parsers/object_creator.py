import datetime


class ObjectCreator(object):
    """
    Gets the retrieved data and outputs an object ready to be
    stored in the DB
    """
    def __init__(self, data_retrieved):
        self._data_retrieved = data_retrieved

    def create(self):
        self._calculate_num_periods()
        list_dates = [x.strftime("%Y-%m-%d") for
                      x in self._data_retrieved[0:self._num_periods]]
        result = dict((dt, dict()) for dt in list_dates)
        for cat_name, v in self._pre_process().iteritems():
            for dt_point, value_point in v.iteritems():
                result[dt_point][cat_name.replace(".", "").
                                 replace(" ", "_").lower()] = value_point
        return result

    def _pre_process(self):
        result = dict()
        list_dates = [x.strftime("%Y-%m-%d") for
                      x in self._data_retrieved[0:self._num_periods]]
        info_retrieved = self._data_retrieved[self._num_periods:]
        for row in info_retrieved:
            result[row[0]] = dict((list_dates[i - 1], row[i])
                                  for i in range(1, self._num_periods + 1))
        return result

    def _calculate_num_periods(self):
        counter = 0
        for x in self._data_retrieved:
            if not isinstance(x, datetime.datetime):
                self._num_periods = counter
                return
            counter += 1
        self._num_periods = counter
