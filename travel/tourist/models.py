from django.db import models
from django import forms

# Create your models here.

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class CommonInfo(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	price = models.FloatField(default=0)
        detail = models.CharField(max_length=500)
        image = models.ImageField(upload_to="images/")
        class Meta:
            verbose_name = "images"
            verbose_name_plural = "images"

        def __unicode__(self):
            return self.name

    	class Meta:
            	abstract = True

class Food(CommonInfo):
	quantity = models.IntegerField(default=0)

class Hotel(CommonInfo):
	KIND_ROOM = (
        ('STD', 'Standard'),
        ('SUP', 'Superopr'),
        ('DLX', 'Deluxe'),
        ('SUT', 'Suite'),
    )
	kindofroom = models.CharField(max_length=3, choices=KIND_ROOM)
	votes = models.IntegerField(default=0)
    # foods = models.ForeignKey(Foods)

class Tourist(CommonInfo):
    hotel = models.ForeignKey(Hotel)
    food = models.ForeignKey(Food)
    means = models.CharField(max_length=200)
