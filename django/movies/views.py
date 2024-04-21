from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm


# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


def detail(request, movie_pk):
    movie = Movie.objects.all(pk=movie_pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'movies/detail.html', context)


def update(request, movie_pk):
    movie = Movie.objects.all(pk=movie_pk)
    
    if request.user != movie.user:
        return redirect('movies: detail', movie.pk)
    
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies: detail', movie.pk)

    else:
        form = MovieForm(instance=movie)

    context = {
        'form': form,
    }
    return render(request, 'movies/update.html', context)


def delete(request, movie_pk):
    movie = Movie.objects.all(pk=movie_pk)
    if request.user != movie.user:
        return redirect('movies: detail', movie.pk)
    
    movie.delete()
    return redirect('movies: index')


def comments_create(request, movie_pk):
    movie = Movie.objects.all(pk=movie_pk)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()

    return redirect('movies: detail', movie.pk)


def comments_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.user != comment.user:
        return redirect('movies:detail', movie_pk)
    
    comment.delete()
    return redirect('movies:detail', movie_pk)


def likes(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)

    return redirect('movies:index')