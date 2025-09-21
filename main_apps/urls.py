from django.urls import path
from . import views

urlpatterns = [
    path('test', views.get, name='get'),
    # Adding the module URL Path    
    path('module/', views.module_list_view, name='module-list'),
    path('module/install/', views.add_module_view, name='install-module'),
    path('module/upgrade/<int:module_id>/', views.edit_module_view, name='upgrade-module'),
    path('module/toggle/<int:module_id>/', views.toggle_module_active_state_view, name='toggle-module'),

]