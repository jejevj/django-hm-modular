from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from main_apps.utils.decorators import role_required

@login_required
@role_required(['manager'])
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        role = request.POST.get('role')

        if form.is_valid() and role in ['manager', 'user']:
            user = form.save()
            profile = user.userprofile
            profile.role = role
            profile.save()
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Form tidak valid atau role tidak dipilih.')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next') or request.POST.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('profile')
        else:
            messages.error(request, 'Username atau password salah.')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {
        'form': form,
        'next': request.GET.get('next', '')
    })


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {
        'user': request.user,
        'profile': request.user.userprofile
    })
