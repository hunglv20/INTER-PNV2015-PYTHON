from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from tourist.models import Tourist
from tourist.models import Food

class IndexView(generic.ListView):
    template_name = 'tourist/index.html'
    context_object_name = 'latest_tourist_list'

    def get_queryset(self):
        return Tourist.objects.all()

class DetailView(generic.ListView):
    template_name = 'tourist/food.html'
    context_object_name = 'latest_food_list'
    def get_queryset(self):
        return Food.objects.all()