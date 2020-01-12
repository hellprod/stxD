from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import ListView

from films.models import Movie


def hello_world(request):
    linki = """
    <ul>
    <li><a href="/">hello PYTHON</a> </li>
    <li><a href="error/">404</a> </li>
    <li><a href="movies/">lista filmów</a> </li>
    </ul>
    """
    return HttpResponse(f"Hello python {linki}")


def error_page(request):
    return render(request, "error_404.html")


class MoviesListAll(ListView):
    model = Movie
    template_name = "movie_list.html"
    context_object_name = "movies"