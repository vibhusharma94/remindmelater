from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from .tasks import send_notification_async


class Reminder(models.Model):

    message = models.TextField()
    email = models.EmailField(max_length=255, null=True, blank=True)
    number = models.CharField(_("Phone Number"), max_length=12, null=True, blank=True)
    scheduled_on = models.DateTimeField()
    is_delivered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reminder"

    def __unicode__(self):
        return self.message

    def delivered(self):
        if not self.is_delivered:
            self.is_delivered = True
            self.save()


# create reminder task in celery after reminder object is created
@receiver(post_save, sender=Reminder)
def create_celery_task(sender, instance, created, **kwargs):
    if created and not instance.is_delivered:
        try:
            send_notification_async.apply_async(
                args=[instance.id], eta=instance.scheduled_on)
        except Exception as e:
            print e.message
