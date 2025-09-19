from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    def test_homepage_status_code(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)

    def test_homepage_uses_correct_template(self):
        # This test assumes your `home` view renders 'home.html'
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home.html")
