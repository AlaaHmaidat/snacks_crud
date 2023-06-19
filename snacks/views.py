from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack


# Create your views here.
class SnackListView(ListView):
    template_name = 'home.html'
    model = Snack
    context_object_name = "snacks"


class SnackDetailView(DetailView):
    template_name = 'detail.html'
    model = Snack
