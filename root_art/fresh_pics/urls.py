from django.urls import path
from . import views

urlpatterns = [
    path('', views.fresh_home, name='fresh_home'),

]
