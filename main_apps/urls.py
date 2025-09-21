from django.urls import path
from . import views

urlpatterns = [
    path('test', views.get, name='get'),
    # Adding the module URL Path    
    path('module/', views.module_list_view, name='module-list'),
    path('module/install/', views.add_module_view, name='install-module'),
    path('module/upgrade/<int:module_id>/', views.edit_module_view, name='upgrade-module'),
    path('module/toggle/<int:module_id>/', views.toggle_module_active_state_view, name='toggle-module'),
    # Adding the product module url
    # path('module/<int:module_id>/products/', views.module_product_list_view, name='module-product-list'),
    # path('module/<int:module_id>/products/add/', views.add_product_view, name='add-product'),
    # path('products/<int:product_id>/edit/', views.edit_product_view, name='edit-product'),
    # path('products/<int:product_id>/delete/', views.delete_product_view, name='delete-product'),

]