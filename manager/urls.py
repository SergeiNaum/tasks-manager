from django.urls import path
from manager import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]
