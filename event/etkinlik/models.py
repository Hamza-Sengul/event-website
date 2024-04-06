from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class SliderItem(models.Model):
    image = models.ImageField(upload_to='slider_images/')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    image = models.ImageField(upload_to='event_images/')
    name = models.CharField(max_length=100)
    description = RichTextField()  # Açıklama alanı eklendi
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Yorumlar(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    isim = models.CharField(max_length=50)
    puan = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    yorum = models.TextField()

    def __str__(self):
        return f"{self.isim[0].upper()}. - {self.puan} yıldız"