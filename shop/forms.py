from django import forms
from .models import Book

class BookCreateForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['title','price','author','synopsis','genre','publisher','publicationDate','image']
		widgets = {
			'publicationDate': forms.TextInput(attrs={'type':'date'}),
		}