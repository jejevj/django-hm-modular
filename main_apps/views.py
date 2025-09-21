from django.http import HttpResponse,Http404
import os, json
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from .models import Module
from .forms import ModuleForm

def get(request):
    return HttpResponse("Hello world!")

MODULES_DIR = os.path.join(settings.BASE_DIR, 'main_apps', 'modules_list')

def module_list_view(request):
    modules = Module.objects.all()
    return render(request, 'modules/module_list.html', {'modules': modules})

def add_module_view(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Module berhasil ditambahkan (install).")
            return redirect('module-list')
    else:
        form = ModuleForm()
    return render(request, 'modules/add_module.html', {'form': form})

def edit_module_view(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    form = ModuleForm(request.POST or None, instance=module)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Module berhasil diubah (upgrade).")
        return redirect('module-list')
    return render(request, 'modules/edit_module.html', {'form': form, 'module': module})

def uninstall_module_view(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    module.is_active = False
    module.save()
    messages.success(request, f"Module '{module.name}' berhasil dilepas (uninstall).")
    return redirect('module-list')

def module_detail_view(request, url_path):
    try:    
        module = Module.objects.get(url_path=url_path, is_active=True)
    except Module.DoesNotExist:
        raise Http404("Modul tidak ditemukan")
    return render(request, 'modules/module_detail.html', {'module': module})

def toggle_module_active_state_view(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    module.is_active = not module.is_active 
    module.save()
    
    if module.is_active:
        messages.success(request, f"Module '{module.name}' berhasil dipasang kembali (reinstall).")
    else:
        messages.success(request, f"Module '{module.name}' berhasil dilepas (uninstall).")

    return redirect('module-list')



