from django.urls import path

from . import views

app_name = 'panel'

urlpatterns = [
    path('index.html', views.statistics, name='statistics'),

]