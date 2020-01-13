from . import views
from .views import BookList, UserBookList, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from django.urls import path


urlpatterns = [
    path('', BookList.as_view(), name='shop-home'),
    path('user/<str:username>', UserBookList.as_view(), name='user-books'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('about/', views.about, name='shop-about'),
]
