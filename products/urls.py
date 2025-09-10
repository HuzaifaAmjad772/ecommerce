from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.product_form, name='product_form'),
    path('detail/<int:id>', views.product_detail, name='product_detail'),
    path('my_listing', views.my_listing, name='my_listing'),
]