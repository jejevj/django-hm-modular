from django.http import HttpResponse,Http404
import os, json
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .models import Module
from .forms import ModuleForm


# Create your views here.

def get(request):
    return HttpResponse("Hello world!")

# modules/views.py

MODULES_DIR = os.path.join(settings.BASE_DIR, 'main_apps', 'modules_list')

# def module_list_view(request):
#     modules = []

#     for module_name in os.listdir(MODULES_DIR):
#         module_path = os.path.join(MODULES_DIR, module_name)
#         module_json_path = os.path.join(module_path, 'module.json')

#         if os.path.exists(module_json_path):
#             with open(module_json_path) as f:
#                 data = json.load(f)
#                 data['name'] = module_name
#                 modules.append(data)

#     return render(request, 'modules/module_list.html', {'modules': modules})

def module_list_view(request):
    modules = Module.objects.all()
    return render(request, 'modules/module_list.html', {'modules': modules})

def add_module_view(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Module added (installed) successfully.")
            return redirect('module-list')
    else:
        form = ModuleForm()
    return render(request, 'modules/add_module.html', {'form': form})


def module_detail_view(request, url_path):
    try:
        module = Module.objects.get(url_path=url_path)
    except Module.DoesNotExist:
        raise Http404("Module not found")

    return render(request, 'modules/module_detail.html', {'module': module})
