from django.urls import path
from . import views

urlpatterns = [
    path('product/add/', views.product_form, name='form'),
    path('detail/<int:id>', views.product_detail, name='product_detail')
]