from django.test import TestCase
from django.urls import reverse


class LandingPageTest(TestCase):
    """Example test for status code page and template"""

    def test_get(self):
        response = self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")
        print(response.content)
