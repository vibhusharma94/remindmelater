from rest_framework import serializers
from rest_framework import exceptions
from .models import Reminder


class UnixEpochDateField(serializers.DateTimeField):

    def to_representation(self, value):
        """ Return epoch time for a datetime object or ``None``"""
        import time
        try:
            return int(time.mktime(value.timetuple()))
        except (AttributeError, TypeError):
            return None

    def to_internal_value(self, value):
        import datetime
        return datetime.datetime.fromtimestamp(int(value))


class ReminderSerializer(serializers.ModelSerializer):
    scheduled_on = UnixEpochDateField()  # scheduled_on is epoch date

    class Meta:
        model = Reminder

    def validate(self, val):
        email = val.get("email")
        number = val.get("number")
        if not email and not number:
            raise exceptions.ValidationError('Either email or number is required')
        return val

    def validate_scheduled_on(self, val):
        import datetime
        now = datetime.datetime.now()
        if val < now:
            raise exceptions.ValidationError(
                'scheduled_on can not be less than current date')
        return val
