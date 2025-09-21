from django.http import HttpResponseForbidden
from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.error(request, "Anda harus login.")
                return redirect('login')

            if hasattr(request.user, 'userprofile'):
                user_role = request.user.userprofile.role
                if user_role in allowed_roles:
                    return view_func(request, *args, **kwargs)

            messages.error(request, "Akses ditolak: Anda tidak memiliki izin.")
            return redirect('module-list')
        return _wrapped_view
    return decorator
