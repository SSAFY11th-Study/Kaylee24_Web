from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        field = '__all__'
        exclude = ('user', 'created_at', 'updated_at', )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        field = '__all__'
        exclude = ('user', 'movie', )
