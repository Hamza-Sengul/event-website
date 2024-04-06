from django.contrib import admin

# Register your models here.
from ckeditor.widgets import CKEditorWidget
from .models import SliderItem, Event, Category, Yorumlar
from django import forms 

class EventAdminForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
        }

class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm

admin.site.register(Event, EventAdmin)
admin.site.register(SliderItem)
admin.site.register(Category)
admin.site.register(Yorumlar)
