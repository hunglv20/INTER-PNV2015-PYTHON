from django.conf.urls import patterns, url

from tourist import views

urlpatterns = patterns('',
    url(r'^index/', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.FoodView.as_view(), name='food'),
    url(r'^(?P<pk>\d+)/hotel/$', views.HotelView.as_view(), name='hotel'),
    url(r'^$',views.IndexViewD.as_view(), name='home'),
    url(r'^about/$', views.AboutViewD.as_view(), name='about'),
    url(r'^food/$', views.FoodViewD.as_view(), name='foodD'),
    url(r'^hotel/$', views.HotelViewD.as_view(), name='hotelD'),
    url(r'^contact/$', views.ContactViewD.as_view(), name='contact'),
    url(r'^detail/$', views.DetailViewD.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)