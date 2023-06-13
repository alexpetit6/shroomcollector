from django.shortcuts import render
from .models import Shroom
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    return render(request, 'shrooms/show.html', {
        'shroom': shroom
    })

class ShroomCreate(CreateView):
    model = Shroom
    fields = '__all__'

class ShroomUpdate(UpdateView):
    model = Shroom
    fields = '__all__'

class ShroomDelete(DeleteView):
    model = Shroom
    success_url = 'shrooms/'