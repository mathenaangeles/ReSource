"""

This is a course requirement for CS 192 Software Engineering II under the
supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer
Science, College of Engineering, University of the Philippines, Diliman for the AY 2019-2020.

© Mathena Angeles

"""
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
    	import users.signals
