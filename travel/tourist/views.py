from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from tourist.models import Tourist
from tourist.models import Food
from tourist.models import Hotel


class FoodView(generic.ListView):
    template_name = 'tourist/food.html'
    context_object_name = 'latest_food_list'
    def get_queryset(self):
        return Food.objects.all()

class MeFoodView(generic.ListView):
    template_name = 'tourist/food.html'
    context_object_name = 'latest_food_list'
    def get_queryset(self):
        return Food.objects.all()

class HotelView(generic.ListView):
    template_name = 'tourist/hotel.html'
    context_object_name = 'latest_hotel_list'
    def get_queryset(self):
        return Hotel.objects.all()

class MeHotelView(generic.ListView):
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

#######################################################

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from tourist.models import Tourist



class TouristForm(ModelForm):
    class Meta:
        model = Tourist
        fields = ['name', 'address', 'price', 'means', 'detail', 'image', 'hotel', 'food']

class IndexView(generic.ListView):
    template_name = 'tourist/index.html'
    context_object_name = 'latest_tourist_list'

    def get_queryset(self):
        return Tourist.objects.all()

# def tourist_list(request, template_name='tourist/index.html'):
#     tourist = Tourist.objects.all()
#     data = {}
#     data['object_list'] = tourists
#     return render(request, template_name, data)

def tourist_create(request, template_name='tourist/index_form.html'):
    form = TouristForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/tourist/index')
    return render(request, template_name, {'form':form})

def tourist_update(request, pk, template_name='tourist/index_form.html'):
    tourist = get_object_or_404(Tourist, pk=pk)
    form = TouristForm(request.POST or None, request.FILES or None, instance=tourist)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/tourist/index')
    return render(request, template_name, {'form':form})

# def product_update(request, pk, template_name='laptop/product_form.html'):
#     pro = get_object_or_404(Product, pk=pk)
#     form = ProductForm(request.POST or None, instance=pro)
#     if form.is_valid():
#         form.save()
#         return redirect('product_list')
#     return render(request, template_name, {'form':form})

def tourist_delete(request, pk, template_name='tourist/tourist_confirm_delete.html'):
    tourist = get_object_or_404(Tourist, pk=pk)    
    if request.method=='POST':
        tourist.delete()
        return HttpResponseRedirect('/tourist/index')
    return render(request, template_name, {'object':tourist})

