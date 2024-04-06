from django import forms
from .models import SliderItem, Event, Category, Yorumlar

class SliderItemForm(forms.ModelForm):
    class Meta:
        model = SliderItem
        fields = ['title', 'description', 'image']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'price', 'location', 'category']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class YorumForm(forms.ModelForm):
    class Meta:
        model = Yorumlar
        fields = ['isim', 'puan', 'yorum']
