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

	"""

	get_queryset method (Created on 1/20/20) -  This method returns the queryset that will be used to 
	retrieve the object that this view will display. It takes in the instance of the class itself. It 
	allows buyers to filter the search results by author, title, genre, and price.

	"""

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

	"""

	get_context_data method (Created on 1/20/20) -  This method populates a dictionary that will be used
	as the template context. In this case, the context it returns contains the user associated with the
	class instance initially passed into the method.

	"""

	def get_context_data(self, **kwargs):
		context = super(UserBookList,self).get_context_data(**kwargs)
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		context['user'] = user
		return context

	"""

	get_queryset method (Created on 1/20/20) -  This method returns the queryset that will be used to 
	retrieve the object that this view will display. It takes in the instance of the class itself. It 
	returns all the book listings posted by a certain seller. 

	"""

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Book.objects.filter(seller=user).order_by('-timestamp')

class BookDetailView(LoginRequiredMixin, DetailView):
	model = Book

class BookCreateView(LoginRequiredMixin, CreateView):
	model = Book
	form_class = BookCreateForm

	"""

	form_valid method (Created on 1/20/20) -  This method checks if the user performing the 
	action is the current logged-in user themself. It returns the form to be saved.

	"""

	def form_valid(self,form):
		form.instance.seller = self.request.user
		return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Book
	form_class = BookCreateForm

	"""

	form_valid method (Created on 1/22/20) -  Re: form_valid method in BookCreateView

	"""

	def form_valid(self,form):
		form.instance.seller = self.request.user
		return super().form_valid(form)

	"""

	test_func method (Created on 1/22/20) -  This method checks if the seller associated with 
	a particular listing is the current logged-in user themself. It returns a boolean value of
	either True or False.

	"""

	def test_func(self):
		book = self.get_object()
		if self.request.user == book.seller:
			return True
		return False


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Book
	success_url = '/'

	"""

	test_func method (Created on 1/24/20) -  Re: test_func method in BookUpdateView

	"""

	def test_func(self):
		book = self.get_object()
		if self.request.user == book.seller:
			return True
		return False

def about(request):
	return render(request,'shop/about.html') 