from .models import Book
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class BookList(ListView):
	model = Book
	paginate_by = 6

	def get_queryset(self):
		query = self.request.GET.get('q')
		if query:
			object_list = self.model.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(genre__icontains=query))
		else:
			object_list = self.model.objects.all().order_by('-timestamp')
		return object_list

class UserBookList(ListView):
	model = Book
	template_name = 'shop/user_books.html'
	ordering = ['-timestamp']
	paginate_by = 6

	def get_queryset(self):
		user = get_object_or_404 (User, username=self.kwargs.get('username'))
		return Book.objects.filter(seller=user).order_by('-timestamp')

class BookDetailView(LoginRequiredMixin, DetailView):
	model = Book

class BookCreateView(LoginRequiredMixin, CreateView):
	model = Book
	fields = ['title','price','author','synopsis','genre','publisher','publicationDate','image']

	def form_valid(self,form):
		form.instance.seller = self.request.user
		return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Book
	fields = ['title','price','author','synopsis','genre','publisher','publicationDate','image']

	def form_valid(self,form):
		form.instance.seller = self.request.user
		return super().form_valid(form)

	def test_func(self):
		book = self.get_object()
		if self.request.user == book.seller:
			return True
		return False

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Book
	success_url = '/'

	def test_func(self):
		book = self.get_object()
		if self.request.user == book.seller:
			return True
		return False

def about(request):
	return render(request,'shop/about.html') 