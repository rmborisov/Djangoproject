from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('singers', views.singers, name='singers'),
    path('create', views.create, name='create'),
]