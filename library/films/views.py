from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from films.models import Movie, Genre

from films.forms import MovieForm, GenreForm


def hello_world(request):
    linki = """
    <ul>
    <li><a href="/">hello PYTHON</a> </li>
    <li><a href="error/">404</a> </li>
    <li><a href="movies/">lista filmów</a> </li>
    <li><a href="genres/">lista gatunków</a> </li>
    </ul>
    """
    return HttpResponse(f"Hello python {linki}")


def error_page(request):
    return render(request, "error_404.html")


class MoviesListAll(ListView):
    model = Movie
    template_name = "movie_list.html"
    context_object_name = "movies"


class PostCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    success_url = "/movie/add"
    template_name = "movie_add.html"


class PostUpdateMovieView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = "movie_update.html"
    success_url = "/movies"


class PostDeleteMovieView(DeleteView):
    model = MovieForm
    template_name = "movie_delete.html"
    success_url = '/movies'


class GenreListAll(ListView):
    model = Genre
    template_name = "genre_list.html"
    context_object_name = "genres"


class PostCreateGenreView(CreateView):
    model = Genre
    form_class = GenreForm
    success_url = "/genres"
    template_name = "genre_add.html"


class PostUpdateGenreView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = "genre_update.html"
    success_url = "/genres"


class PostDeleteGenreView(DeleteView):
    model = Genre
    template_name = "genre_delete.html"
    success_url = '/genres'

