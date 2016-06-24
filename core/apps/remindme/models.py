from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from .tasks import send_notification_async


class Reminder(models.Model):

    message = models.TextField()
    # we don't need email or number here.
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


# Basic approach
class Channel(models.Model):

    EMAIL = 1
    SMS = 2
    ANDROID = 3
    IOS = 4
    TWITTER = 5
    TYPE_CHOICES = (
        (EMAIL, 'EMAIL'),
        (SMS, "SMS"),
        (ANDROID, "ANDROID"),
        (IOS, "IOS"),
        (TWITTER, "TWITTER"),
    )

    reminder = models.ForeignKey(Reminder)

    # Medium to deliver notification
    c_type = models.IntegerField(_("Channel Type"), choices=TYPE_CHOICES)
    # channel_value could be a Phone number, Email , Android or Ios device id or twiiter username.
    # validation can be done in serializer. This is directly depends on type of channel.
    # e.g in case of android push notification device id and registration key is required.
    # note: only one c_value might not be sufficient to deliver message.
    c_value = models.CharField(_("Channel Value"), max_length=255)
    # This way we can track delivery status for each channel
    is_delivered = models.BooleanField(default=False)
