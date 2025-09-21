from django.http import HttpResponse
import os, json
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

# Create your views here.

def get(request):
    return HttpResponse("Hello world!")

# modules/views.py

MODULES_DIR = os.path.join(settings.BASE_DIR, 'main_apps', 'modules_list')

def module_list_view(request):
    modules = []

    for module_name in os.listdir(MODULES_DIR):
        module_path = os.path.join(MODULES_DIR, module_name)
        module_json_path = os.path.join(module_path, 'module.json')

        if os.path.exists(module_json_path):
            with open(module_json_path) as f:
                data = json.load(f)
                data['name'] = module_name
                modules.append(data)

    return render(request, 'modules/module_list.html', {'modules': modules})


def install_module(request, module_name):
    try:
        module_path = os.path.join(MODULES_DIR, module_name, 'install.py')
        exec(open(module_path).read(), {})
        messages.success(request, f"Module '{module_name}' installed successfully.")
    except Exception as e:
        messages.error(request, f"Error installing module: {str(e)}")

    return redirect('module-list')
