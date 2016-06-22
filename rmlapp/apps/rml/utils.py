import datetime
import time


class Utilities(object):

    @staticmethod
    def date_to_string(timestamp):
        return timestamp.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def epoch_to_date(epoch):
        return datetime.datetime.fromtimestamp(float(epoch))

    @staticmethod
    def date_to_epoch(_date):
        return int(time.mktime(_date.timetuple()))
