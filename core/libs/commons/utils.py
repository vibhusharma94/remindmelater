import datetime
import time


def get_default_django_settings_module():
    default_django_settings_module = "core.settings.dev"
    return default_django_settings_module


def epoch_to_date(epoch):
    return datetime.datetime.fromtimestamp(float(epoch))


def date_to_epoch(_date):
    return int(time.mktime(_date.timetuple()))
