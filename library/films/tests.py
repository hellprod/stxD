from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
# Create your tests here.
from films.forms import MovieForm
from films.models import Genre, Movie
from films.views import hello_world


class MyTests(TestCase):
    def test_my_response(self):
        status = 200
        self.assertEqual(status, 200)

    def test_my(self):
        status = 201
        self.assertEqual(status, 201)


class SimpleTestCase(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name='Horror')
        self.movie = Movie.objects.create(
            name='Dracula',
            year=1987,
            summary='02-11-1987',
            Genre=self.genre,
        )

    def tearDown(self):
        self.movie.delete()
        self.genre.delete()

    def test_max_length(self):
        form = MovieForm(data={'name': 'X'*200})
        self.assertFalse(form.is_valid())

    def test_initial(self):
        form = MovieForm(instance = self.movie)
        self.assertEqual(form.initial['name'], self.movie.name)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, hello_world)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = hello_world(request)
        # self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<li><a href="error/">404</a> </li>', response.content)
        # self.assertTrue(response.content.endswith(b'</html>'))
