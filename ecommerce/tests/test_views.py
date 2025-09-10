from django.test import TestCase
from django.urls import reverse

class HomeViewTest(TestCase):
    def test_homepage_status_code(self):
        resp = self.client.get(reverse("home"))  # adjust if home URL is named differently
        self.assertEqual(resp.status_code, 200)
