from datetime import datetime, timedelta
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.core.urlresolvers import reverse
from .utils import Utilities


class RMLTestCase(APITestCase):
    def setUp(self):

        self.api_client = APIClient()

    def test_reminder_success(self):
        """
        Add Reminder success
        """
        scheduled_on = datetime.now() + timedelta(0, 60)  # 60 secs from now
        epoch = Utilities.date_to_epoch(scheduled_on)
        payload = {"message": "It's working",
                   "email": "vibhuindian@gmail.com",
                   "number": 7022158873,
                   "scheduled_on": epoch}
        url = reverse('add-reminder', kwargs={})
        response = self.api_client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reminder_failed(self):
        """
        Add Reminder Failed: invalid payload
        """
        payload = {}
        url = reverse('add-reminder', kwargs={})
        response = self.api_client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
