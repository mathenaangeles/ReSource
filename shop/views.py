from .models import Book
from itertools import chain
from django.db.models import Q
from users.models import Profile
from .forms import BookCreateForm
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
		title = self.request.GET.get('title')
		author = self.request.GET.get('author')
		genre = self.request.GET.get('genre')
		minimum = self.request.GET.get('min')
		maximum = self.request.GET.get('max')

		if title:
			object_list = self.model.objects.filter(Q(title__icontains=title))
		else:
			object_list = self.model.objects.all().order_by('-timestamp')

		if author:
			object_list = object_list & self.model.objects.filter(Q(author__icontains=author))

		if genre:
			object_list = object_list & self.model.objects.filter(Q(genre__icontains=genre))

		if minimum:
			object_list = object_list & self.model.objects.filter(Q(price__gte=minimum))

		if maximum:
			object_list = object_list & self.model.objects.filter(Q(price__lte=maximum))
	
		return object_list

class UserBookList(ListView):
	model = Book
	template_name = 'shop/user_books.html'
	ordering = ['-timestamp']
	paginate_by = 6

	def get_context_data(self, **kwargs):
		context = super(UserBookList,self).get_context_data(**kwargs)
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		context['user'] = user
		return context

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Book.objects.filter(seller=user).order_by('-timestamp')

class BookDetailView(LoginRequiredMixin, DetailView):
	model = Book

class BookCreateView(LoginRequiredMixin, CreateView):
	model = Book
	form_class = BookCreateForm

	def form_valid(self,form):
		form.instance.seller = self.request.user
		return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Book
	form_class = BookCreateForm

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