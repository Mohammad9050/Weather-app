from django import urls
from django.urls import path
from django.views.generic import TemplateView

from . import views
app_name = 'Home'
urlpatterns = [
    path('', views.weather_show, name='home'),
    path('update/<int:num>', views.update_obj, name='update'),
    path('delete/<int:num>', views.delete_obj, name='delete'),

]