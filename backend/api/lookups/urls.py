from django.urls import path

from . import views

urlpatterns = [
    path('cities/', views.CityListView.as_view(), name='city-list'),
]