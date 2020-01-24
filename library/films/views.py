from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from films.models import Movie, Genre
from films.forms import MovieForm, GenreForm
#api
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, filters
from films.serializers import UserSerializer, GroupSerializer
#myapi
from films.serializers import MovieSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


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
    success_url = "/movies"
    template_name = "movie_add.html"


class PostUpdateMovieView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = "movie_update.html"
    success_url = "/movies"


class PostDeleteMovieView(DeleteView):
    model = Movie
    template_name = "movie_delete.html"
    success_url = '/movies'
#


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


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# class MovieViewSet(viewsets.ModelViewSet):
class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ("name", "year", "summary")
    # search_fields = ('name', "year")
    # ordering_fields = ("year",)

    def get_queryset(self):
        queryset = self.queryset
        return queryset

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = MovieSerializer(instance)
    #     return Response(serializer.data)
    #
    # def create(self, request, *args, **kwargs):
    #     if request.user.is_staff:
    #         return super().create(request, *args, **kwargs)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)