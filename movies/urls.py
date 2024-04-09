
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_movie/', views.create_movie, name="create_movie"),
    path('<str:movie>', views.movie_detail, name="movie_detail"),
]
