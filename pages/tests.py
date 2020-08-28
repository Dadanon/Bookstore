from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView


class PagesTestCase(SimpleTestCase):

    def setUp(self) -> None:
        url = reverse('home')
        self.response = self.client.get(url)

    def test_html_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_html_template_used(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_content_used(self):
        self.assertContains(self.response, 'Hi, buddy!')

    def test_no_content_used(self):
        self.assertNotContains(self.response, 'Hello, world!')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )

# Create your tests here.
