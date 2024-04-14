from django.urls import path
from .views import AuthorREST, FavouriteAuthorREST


urlpatterns = [
    path('author/', AuthorREST.as_view()),
    path('favourite_author/',FavouriteAuthorREST.as_view()),
    path('favourite_author/<int:id>/', FavouriteAuthorREST.as_view()),
    path('author/<int:id>/', AuthorREST.as_view()),
]