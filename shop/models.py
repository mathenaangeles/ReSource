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

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book-detail',kwargs={'pk': self.pk})