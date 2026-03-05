from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CareForm
from .models import Plant, Category

# Create your views here.

class Home(LoginView): 
   template_name = 'home.html'

class PlantList(LoginRequiredMixin, ListView):
    model = Plant

    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user)

class PlantCreate(LoginRequiredMixin, CreateView):
    model = Plant
    fields = ['name', 'size', 'notes', 'categories', 'image_url'] 
    
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class PlantDetail(LoginRequiredMixin, DetailView):
    model = Plant

    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['care_form'] = CareForm()
        return context 

class PlantUpdate(LoginRequiredMixin, UpdateView):
    model = Plant
    fields = ['name', 'size', 'notes', 'categories', 'image_url'] 

class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = '/plants/'

@login_required
def add_care(request, pk):
    form = CareForm(request.POST)
    if form.is_valid(): 
        new_care = form.save(commit = False)
        new_care.plant_id = pk
        new_care.save()
    return redirect('plant-detail', pk=pk)

class CategoryList(LoginRequiredMixin, ListView): 
    model = Category

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

class CategoryCreate(LoginRequiredMixin, CreateView): 
    model = Category 
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CategoryDetail(LoginRequiredMixin, DetailView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

class CategoryUpdate(LoginRequiredMixin, UpdateView): 
    model = Category
    fields = ['name', 'description']

class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = '/categories/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('plant-list')
        else: 
            error_message = 'invalid sign up'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context) 
    
