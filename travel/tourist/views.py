from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from tourist.models import Tourist
from tourist.models import Food
from tourist.models import Hotel

class IndexView(generic.ListView):
    template_name = 'tourist/index.html'
    context_object_name = 'latest_tourist_list'

    def get_queryset(self):
        return Tourist.objects.all()

class FoodView(generic.ListView):
    template_name = 'tourist/food.html'
    context_object_name = 'latest_food_list'
    def get_queryset(self):
        return Food.objects.all()

class HotelView(generic.ListView):
    template_name = 'tourist/hotel.html'
    context_object_name = 'latest_hotel_list'
    def get_queryset(self):
        return Hotel.objects.all()

######################################################

class IndexViewD(generic.ListView):
    template_name = 'web/index.html'
    context_object_name = 'latest_tourist_list'
    def get_queryset(self):
        return Tourist.objects.order_by('-id')[:3]
    # def delete(request):
    # query = Tourist.objects.get(pk=id)
    # query.delete()
    # return HttpResponse("Deleted!")

class AboutViewD(generic.ListView):
    template_name = 'web/about.html'
    context_object_name = 'latest_tourist_list'
    def get_queryset(self):
        return Tourist.objects.order_by('-id')[:3]

class FoodViewD(generic.ListView):
    template_name = 'web/food.html'
    context_object_name = 'latest_food_list'
    def get_queryset(self):
        return Food.objects.order_by('-id')[:3]


class HotelViewD(generic.ListView):
    template_name = 'web/hotel.html'
    context_object_name = 'latest_hotel_list'
    def get_queryset(self):
        return Hotel.objects.all()

class ContactViewD(generic.ListView):
    template_name = 'web/contact.html'
    context_object_name = 'latest_tourist_list'
    def get_queryset(self):
        return Tourist.objects.order_by('-id')[:3]

class DetailViewD(generic.ListView):
    template_name = 'web/detail.html'
    context_object_name = 'latest_tourist_list'
    def get_queryset(self):
        return Tourist.objects.order_by('-id')[:3]



