from django.contrib import admin
from .models import Reminder


class ReminderAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'number', 'email', 'scheduled_on')
    list_filter = ('is_delivered',)


admin.site.register(Reminder, ReminderAdmin)
