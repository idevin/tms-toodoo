"""toodoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index),
    path('create_list', views.create_list, name='create_list'),
    path('store_list', views.store_list, name='store_list'),
    path('edit_list/<list_id>', views.edit_list, name='edit_list'),
    path('update_list/<list_id>', views.update_list, name='update_list'),
    path('destroy_list/<list_id>', views.destroy_list, name='destroy_list'),
    path('create_note/<list_id>', views.create_note, name='create_note')
]
