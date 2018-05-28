from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/(?P<)', views.index, name='index')
]