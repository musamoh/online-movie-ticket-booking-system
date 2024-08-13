from django.urls import path
from .views import MovieListView, movie_details

app_name = 'movie'

urlpatterns = [
    
    path(r'', MovieListView.as_view(), name='list'),
    path(r'<movie_id>/', movie_details, name='detail'),
        
]