from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shroom
from .forms import OriginForm

# shrooms = [
#     {sci_name= 'Psilocybe cyanescens', common_name= 'Wavy Caps', edible= True, properties= 'psychoactive'},
#     {sci_name= 'Clitocybe nebularis', common_name= 'Clouded Funnel', edible= False, properties= 'aesthetic'},
#     {sci_name= 'Morchella esculenta', common_name= 'Yellow Morel', edible: True, properties: 'delicious'}
# ]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shrooms_index(request):
    shrooms = Shroom.objects.all()
    return render(request, 'shrooms/index.html', {
        'shrooms': shrooms
    })

def shrooms_show(request, shroom_id):
    shroom = Shroom.objects.get(id=shroom_id)
    origin_form = OriginForm()
    return render(request, 'shrooms/show.html', {
        'shroom': shroom,
        'origin_form': origin_form
    })

class ShroomCreate(CreateView):
    model = Shroom
    fields = '__all__'

class ShroomUpdate(UpdateView):
    model = Shroom
    fields = '__all__'

class ShroomDelete(DeleteView):
    model = Shroom
    success_url = '/shrooms'

def add_origin(request, shroom_id):
    form = OriginForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
        new_origin = form.save(commit=False)
        new_origin.shroom_id = shroom_id
        new_origin.save()
    return redirect('show', shroom_id=shroom_id)