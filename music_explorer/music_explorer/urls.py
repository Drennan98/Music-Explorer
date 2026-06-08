"""
URL configuration for music_explorer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# urlpatterns is a list of routes and each route tells Django that when you visit
# said URL, take them to that part of the app. 
urlpatterns = [
    # This sends anything starting with /admin/ to the admin site, and anything starting with / to the explorer app.
    path('admin/', admin.site.urls),
    # So instead of defining all URL's here we can just include the URL's from the explorer app.
    path('', include('explorer.urls'))
]
