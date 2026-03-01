from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.http import HttpResponse

from .models import Plant

# Create your views here.

def home(request): 
    return render(request, 'home.html')

class PlantList(ListView):
    model = Plant


class PlantCreate(CreateView):
    model = Plant
    fields = ['name', 'size', 'notes'] #'categories' commented out while none are available
    

    def form_valid(self, form):
        return super().form_valid(form)

class PlantDetail(DetailView):
    model = Plant
