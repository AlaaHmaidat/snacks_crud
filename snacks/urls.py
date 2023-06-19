from django.contrib import admin
from django.urls import path
from .views import SnackListView,SnackDetailView

urlpatterns = [
    path('', SnackListView.as_view(), name='home'),
    path('detail', SnackDetailView.as_view(), name='detail'),
]
