from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('PymongoView', views.PymongoView.as_view()),
    path('get_todo', views.get_todo),


]
