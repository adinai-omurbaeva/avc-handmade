from django import forms
from .models import Comment, Purchase, CustomPurchase

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email', 'body')

class CartCreationForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('count',)

class CustomPurchaseForm(forms.ModelForm):
    class Meta:
        model = CustomPurchase
        fields = ('image1', 'image2', 'image3', 'size', 'description')
