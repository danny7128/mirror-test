from django.urls import path
from . import views

app_name = "pjt1"

urlpatterns = [
    path("", views.index, name="index"),
    path("review/", views.review, name="review"),
    path("create/", views.create, name="create"),
]
