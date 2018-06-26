from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create_post/', views.create_post, name='create_post'),
    path('post_details/<int:id>/', views.post_details, name='post_details'),
    path('update_post/<int:id>/', views.update_post, name='update_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post')
]