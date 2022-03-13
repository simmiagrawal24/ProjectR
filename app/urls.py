from django.urls import path
from . import views

urlpatterns= [
    path('findproj/', views.find_proj),
    path('prof/', views.profile),
    path('request/', views.req),
    path('home/', views.home),
    path('login/', views.login),
    path('select/', views.sel),
    path('track/', views.track),
    path('create/', views.create),
    path('inter/', views.inter),
    path('search/', views.search),
    path('ser/', views.ser)
]