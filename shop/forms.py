from django import forms
from .models import Comment, Purchase

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email', 'body')

class CartCreationForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('count',)