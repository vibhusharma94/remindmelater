from django.conf import settings
from django.core.mail import send_mail
import requests


class MessagePipeline(object):
    """ Implement channel specific logic """

    def __init__(self, reminder):
        self.reminder = reminder

    def send(self):
        if self.reminder.email:
            self.send_email_notification()
        if self.reminder.number:
            self.send_sms_notification()

    def send_sms_notification(self):

        country = 91
        mobile = self.reminder.number
        message = self.reminder.message
        auth_key = "110273ALmQkxJZx5710fb0c"  # msg91 auth key here
        sender_id = 'RMLIND'  # your senderID
        route = 4
        sms_url = 'https://control.msg91.com/api/sendhttp.php'

        params = {'authkey': auth_key,
                  'mobiles': mobile,
                  'message': message,
                  'sender': sender_id,
                  'route': route,
                  'country': country,
                  'response': 'json'}
        try:
            requests.get(sms_url, params=params)
        except Exception as e:
            print e.message
        else:
            self.reminder.delivered()
            print "sms sent to %s" % (mobile)

    def send_email_notification(self):
        subject = "Reminder"
        message = self.reminder.message
        to_email = self.reminder.email
        try:
            send_mail(
                subject, message,
                settings.DEFAULT_FROM_EMAIL, [to_email])
        except Exception as e:
            print str(e)
        else:
            self.reminder.delivered()
            print "mail sent to %s" % (to_email)

    def send_facebook_notification(self):
        pass

    def send_twitter_notification(self):
        pass

    def send_whatsapp_notification(self):
        pass
