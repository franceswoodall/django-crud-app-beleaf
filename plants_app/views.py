from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm 

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
        form.instance.user = self.request.user 
        return super().form_valid(form)

class PlantDetail(DetailView):
    model = Plant

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['name', 'size', 'notes']

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'

