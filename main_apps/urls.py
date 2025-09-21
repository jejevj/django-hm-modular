from django.urls import path
from . import views

urlpatterns = [
    path('test', views.get, name='get'),
    # Adding the module URL Path    
    path('module/', views.module_list_view, name='module-list'),
    path('module/install/', views.add_module_view, name='install-module'),
]