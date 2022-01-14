from django.test import SimpleTestCase
from django.urls import resolve, reverse

from .views import AboutPageView, HomePageView


class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi Luke, I am your father')

    def test_homepage_resolves_homepageview(self):
        view = resolve(reverse('home'))
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_correct_html(self):
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve(reverse('about'))
        self.assertEqual(
                view.func.__name__,
                AboutPageView.as_view().__name__
        )
