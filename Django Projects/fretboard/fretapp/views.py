from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tuning

def index(request):
    tunings = Tuning.objects.all()
    return render(request, 'fretapp/index.html', {'tunings': tunings})

def index_vue(request):
    return render(request, 'blog/index_vue.html')

def get_tuning(request):
    tunings = Tuning.objects.all()
    tuning_data = []
    for tuning in tunings:
        tuning_data.append({
            'id': tuning.id,
            'name': tuning.name,
            'root': tuning.root
        })
    return JsonResponse({'tunings': tuning_data})