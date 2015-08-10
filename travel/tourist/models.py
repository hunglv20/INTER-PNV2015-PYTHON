from django.db import models

# Create your models here.
class CommonInfo(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	price = models.FloatField(default=0)
	# image = models.ImageField()

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


# class Poll(models.Model):
#     question = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

# class Choice(models.Model):
#     poll = models.ForeignKey(Poll)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)