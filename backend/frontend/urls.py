from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('users', views.index),
    path('scores', views.index),
    path('courses', views.index)
]