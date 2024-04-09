from django.shortcuts import render

# Create your views here.
def index(request):
    print(request.GET)
    movie = request.GET.get('movie')
    context = {
        'movie': movie
    }

    return render(request, 'movies/index.html', context)


def create_movie(request):
    return render(request, 'movies/create_movie.html')


def movie_detail(request, movie):
    context = {
        'movie': movie
    }
    return render(request, 'movies/movie_detail.html', context)


