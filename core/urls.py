from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('program/', lambda request: redirect('programs', permanent=True)),
    path('programs/', views.programs, name='programs'),
    path('events/', views.events, name='events'),
    path('all-events/', views.all_events, name='all_events'),
    path('events/<slug:slug>/', views.events_detail, name='events_detail'),
    path('hosts/', views.hosts, name='hosts'),
    path('talent/', views.talent, name='talent'),
    path('talent/<slug:slug>/', views.talent_detail, name='talent_detail'),
    path('partner/', lambda request: redirect('partnerships', permanent=True)),
    path('partnerships/', views.partnerships, name='partnerships'),
    path('media-gallery/', views.media_gallery, name='media_gallery'),
    path('media-gallery/<slug:slug>/', views.media_detail, name='media_detail'),
    path('all-media/', views.all_media, name='all_media'),
    path('news/', views.news, name='news'),
    path('blog/', views.blog, name='blog'),
    path('blog/all/', views.blog_all, name='blog_all'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('apply/', views.apply, name='apply'),
    path('radio/stream/', views.radio_stream, name='radio_stream'),
    path('order-equipment/', views.order_equipment, name='order_equipment'),
]
