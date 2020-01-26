"""

This is a course requirement for CS 192 Software Engineering II under the
supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer
Science, College of Engineering, University of the Philippines, Diliman for the AY 2019-2020.

© Mathena Angeles

Code History:

1/21/20 - First Sprint - Created the create_profile and save_profile Methods

"""
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

"""

create_profile method (Created on 1/21/20) -  This method receives the signal from the user that a
profile must be created.

"""

@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)

"""

save_profile method (Created on 1/21/20) -  This method receives the signal from the user that a
profile must be saved.

"""

@receiver(post_save, sender=User)
def save_profile(sender,instance,created,**kwargs):
	instance.profile.save()