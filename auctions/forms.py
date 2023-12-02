from django.forms import ModelForm
from django import forms
from .models import Listing


class NewListingForm(ModelForm):
    # title
    listing_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    # text-based description
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Description', 'rows': 4, 'cols': 40}))
    # starting bid price
    min_price = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': 'Price'}))
    # optionally image URL
    image = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Image URL'}), blank=True)
    # optionally category
    category = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Category'}), blank=True)

    class Meta:
        model = Listing
        fields = ['listing_title', 'description', 'min_price', 'image', 'category']
