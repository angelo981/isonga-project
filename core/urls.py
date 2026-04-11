from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('programs/', views.programs, name='programs'),
    path('events/', views.events, name='events'),
    path('talent/', views.talent, name='talent'),
    path('partnerships/', views.partnerships, name='partnerships'),
    path('media-gallery/', views.media_gallery, name='media_gallery'),
    path('news/', views.news, name='news'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
]
