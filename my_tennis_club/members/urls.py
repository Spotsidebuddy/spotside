from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/all', views.all_members, name='all')
]

