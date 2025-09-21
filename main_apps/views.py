from django.http import HttpResponse,Http404
import os, json
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.forms import inlineformset_factory
from .models import Module, NamaProduct
from .forms import ModuleForm,ProductForm
from .utils.decorators import role_required
from django.contrib.auth.decorators import login_required


ProductFormSet = inlineformset_factory(
    parent_model=Module,
    model=NamaProduct,
    form=ProductForm,
    extra=1,
    can_delete=True
)

def get(request):
    return HttpResponse("Hello world!")

MODULES_DIR = os.path.join(settings.BASE_DIR, 'main_apps', 'modules_list')

@login_required
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

    if request.method == 'POST':
        form = ModuleForm(request.POST, instance=module)
        formset = ProductFormSet(request.POST, instance=module)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, "Modul dan produk berhasil diperbarui.")
            return redirect('upgrade-module', module_id=module.id)
        else:
            if not form.is_valid():
                print("ModuleForm errors:", form.errors)
            if not formset.is_valid():
                print("ProductFormSet errors:", formset.errors)
                for i, f_errors in enumerate(formset.errors):
                    print(f"Product form {i} errors: {f_errors}")

    else:
        form = ModuleForm(instance=module)
        formset = ProductFormSet(instance=module)

    return render(request, 'modules/edit_module.html', {
        'form': form,
        'formset': formset,
        'module': module
    })


def module_detail_view(request, url_path):
    try:    
        module = Module.objects.get(url_path=url_path, is_active=True)
    except Module.DoesNotExist:
        raise Http404("Modul tidak ditemukan")

    products = module.products.all()

    return render(request, 'modules/module_detail.html', {
        'module': module,
        'products': products
    })
@role_required(['manager'])
def toggle_module_active_state_view(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    module.is_active = not module.is_active 
    module.save()
    
    if module.is_active:
        messages.success(request, f"Module '{module.name}' berhasil dipasang kembali (reinstall).")
    else:
        messages.success(request, f"Module '{module.name}' berhasil dilepas (uninstall).")

    return redirect('module-list')

