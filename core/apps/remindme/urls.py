from django.conf.urls import patterns, url
from apps.remindme import views

urlpatterns = patterns(
    '',
    # add reminder url endpoint
    url(r'^add/reminder$', views.ReminderApi.as_view(), name="add-reminder"),
)
