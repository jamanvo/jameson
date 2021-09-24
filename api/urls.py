from django.urls import include
from django.urls import path

app_name = 'api'
urlpatterns = [
    path('movies/', include('api.movies.urls')),
]
