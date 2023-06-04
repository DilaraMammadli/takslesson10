from django import forms
from .models import Book

# class BookForm(forms.Form):
    # name=forms.CharField()
    # author_name=forms.CharField()
    # content=forms.CharField()
class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ("name", "author_name")

    