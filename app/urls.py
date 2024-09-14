from django.urls import path
from .views import home, create, success

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('success/', success, name='success')
]
