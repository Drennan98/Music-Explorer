from django.urls import path
from . import views

# urlpatterns is a list of routes and each route tells Django that when you visit
# said URL, take them to that part of the app. 
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_music, name='search')
]