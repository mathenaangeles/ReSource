"""

This is a course requirement for CS 192 Software Engineering II under the
supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer
Science, College of Engineering, University of the Philippines, Diliman for the AY 2019-2020.

© Mathena Angeles

Code History:

1/20/20 - First Sprint - Added Paths for user-books, book-detail, book-create, about, and home Pages
1/22/20 - " - Added Path for book-update Page
1/24/20 - " - Added Path for book-delete Page

"""
from . import views
from .views import BookList, UserBookList, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', BookList.as_view(), name='shop-home'),
    path('user/<str:username>', UserBookList.as_view(), name='user-books'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', csrf_exempt(BookDeleteView.as_view()), name='book-delete'),
    path('about/', views.about, name='shop-about'),
]
