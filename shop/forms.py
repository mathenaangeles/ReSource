"""

This is a course requirement for CS 192 Software Engineering II under the
supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer
Science, College of Engineering, University of the Philippines, Diliman for the AY 2019-2020.

© Mathena Angeles

Code History:

1/21/20 - First Sprint - Added BookCreateForm

"""
from django import forms
from .models import Book

class BookCreateForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['title','price','author','synopsis','genre','publisher','publicationDate','image']
		widgets = {
			'publicationDate': forms.TextInput(attrs={'type':'date'}),
		}