from celery.decorators import task
from .pipeline import MessagePipeline


@task()
def send_notification_async(reminder_id):
    from .models import Reminder
    try:
        reminder = Reminder.objects.get(id=reminder_id)
    except Exception as e:
        print e.message
    else:
        # initiate pipline class
        msgpipeline = MessagePipeline(reminder)
        msgpipeline.send()
