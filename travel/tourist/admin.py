from django.contrib import admin

# Register your models here.
from tourist.models import Food
admin.site.register(Food)
from tourist.models import Hotel
admin.site.register(Hotel)
from tourist.models import Tourist
admin.site.register(Tourist)
