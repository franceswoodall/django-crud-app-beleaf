from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm 
from .forms import CareForm

from django.http import HttpResponse

from .models import Plant, Care, Category

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['care_form'] = CareForm()
        return context 

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['name', 'size', 'notes']

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'

def add_care(request, pk):
    form = CareForm(request.POST)
    if form.is_valid(): 
        new_care = form.save(commit = False)
        new_care.plant_id = pk
        new_care.save()
    return redirect('plant-detail', pk=pk)

class CategoryList(ListView): 
    model = Category

