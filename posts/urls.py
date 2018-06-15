from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path('', views.post_list, name='list'),
    path('create/', views.post_create, name='create'),
    path('details/<int:id>/', views.post_details, name='details')
]