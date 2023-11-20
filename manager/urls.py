from django.contrib import admin
from django.urls import path
from manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    # path('', views.index, name='index')
]