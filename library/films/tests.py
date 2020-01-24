from django.test import TestCase

# Create your tests here.
from .forms import MovieForm
from .models import Genre, Movie


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