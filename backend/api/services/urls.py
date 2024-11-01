from django.urls import path

from . import views

urlpatterns = [
    path("", views.ServicesCategoriesView.as_view(), name="main-categories"),
]
