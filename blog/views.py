from django.shortcuts import render

# Create your views here.

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

