"""

This is a course requirement for CS 192 Software Engineering II under the
supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer
Science, College of Engineering, University of the Philippines, Diliman for the AY 2019-2020.

© Mathena Angeles

Code History:

1/21/20 - First Sprint - Added Profile Model

"""
from PIL import Image
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	location = models.CharField(max_length=250, blank=True)
	phone = PhoneNumberField(blank=True)
	image = models.ImageField(default='default.jpg', upload_to="profile_pictures")

	"""

	__str__ method (Created on 0/22/20) - This creates a more readable string representation of the object.
	It takes in the instance of the class itself and returns the username of the user.

	"""

	def __str__(self):
		return f'{self.user.username} Profile'

