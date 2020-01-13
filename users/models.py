from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	location = models.CharField(max_length=250, blank=True)
	phone = PhoneNumberField(blank=True)
	image = models.ImageField(default='default.jpg', upload_to="profile_pictures")

	def __str__(self):
		return f'{self.user.username} Profile'

