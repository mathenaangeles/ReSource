"""

This is a course requirement for CS 192 Software Engineering II under the
supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer
Science, College of Engineering, University of the Philippines, Diliman for the AY 2019-2020.

© Mathena Angeles

Code History:

1/21/20 - First Sprint - Added Book Model

"""
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator



class Book(models.Model):
	title = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=8,decimal_places=2, validators=[MinValueValidator(0)])
	author = models.CharField(max_length=255)
	synopsis = models.TextField()
	genre = models.CharField(max_length=255, blank=True)
	publisher = models.CharField(max_length=255, blank=True)
	publicationDate = models.DateField(null=True, blank=True, verbose_name='Publication Date')
	image = models.ImageField(default='default.jpg',upload_to="book_pictures")
	timestamp = models.DateTimeField(default=timezone.now)
	seller = models.ForeignKey(User, on_delete=models.CASCADE)

	"""

	__str__ method (Created on 0/21/20) - This creates a more readable string representation of the object.
	It takes in the instance of the class itself and returns the title of the book.

	"""

	def __str__(self):
		return self.title

	"""

	get_absolute_url method (Created on 0/21/20) - It tell Django how to calculate the canonical URL for an object. 
	It takes in the instance of the class itself return a string that can be used to refer to the object over HTTP.

	"""

	def get_absolute_url(self):
		return reverse('book-detail',kwargs={'pk': self.pk})