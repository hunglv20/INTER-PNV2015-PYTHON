from django.conf.urls import patterns, url

from tourist import views

urlpatterns = patterns('',
    url(r'^index/', views.IndexView.as_view(), name='index'),
    # url(r'^delete/', views.DeleteIndexView.as_view(), name='delete'),
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

    url(r'^new/$', views.tourist_create, name='tourist_new'),
    url(r'^edit/(?P<pk>\d+)$', views.tourist_update, name='tourist_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.tourist_delete, name='tourist_delete'),

    url(r'^mefood/$', views.FoodView.as_view(), name='mefood'),
    url(r'^mehotel/$', views.HotelView.as_view(), name='mehotel'),
)