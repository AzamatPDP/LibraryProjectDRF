from django.urls import path
from .views import BookListApiView, book_list_view, BookDetailApiView, BookDeleteApiView, BookUpdateApiView, \
    BookCreateApiView, BookListCreateApiView, BookUpdateDeleteApiView

urlpatterns = [
    path("", BookListApiView.as_view()),
    path("booklistcreate/",BookListCreateApiView.as_view()),
    path("bookupdatedelete/<int:pk>/",BookUpdateDeleteApiView.as_view()),
    path("books/<int:pk>/", BookDetailApiView.as_view()),
    path("books/<int:pk>/delete/", BookDeleteApiView.as_view()),
    path("books/<int:pk>/update/", BookUpdateApiView.as_view()),
    path("books/create/", BookCreateApiView.as_view()),
    path("books/", book_list_view)
]
