"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import router
from django.urls import path, include

from films.views import hello_world, error_page

from films.views import MoviesListAll, GenreListAll, PostCreateView, PostCreateGenreView, PostUpdateGenreView, \
    PostDeleteGenreView, PostUpdateMovieView, PostDeleteMovieView, UserViewSet, MovieViewSet, UserViewSet, GroupViewSet
#api
from rest_framework import routers

from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('api-movies', MovieViewSet, base_name='s')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
    path('error/', error_page),
    path('movies/', MoviesListAll.as_view(), ),
    path('movie/add/', PostCreateView.as_view(), ),
    path('genres/', GenreListAll.as_view(), name="genre_list"),
    path('genre/add', PostCreateGenreView.as_view(), ),
    path('genre/update/<int:pk>', PostUpdateGenreView.as_view(), name="genre_edit"),
    path('movie/update/<int:pk>', PostUpdateMovieView.as_view(), name="movie_edit"),
    path('genre/delete/<int:pk>', PostDeleteGenreView.as_view(), name="genre_delete"),
    path('movie/delete/<int:pk>', PostDeleteMovieView.as_view(), name="movie_delete"),
    path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-movies/', views.obtain_auth_token),
]
