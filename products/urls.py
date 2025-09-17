from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.product_form, name='product_form'),
    path('detail/<int:id>', views.product_detail, name='product_detail'),
    path('my_listing', views.my_listing, name='my_listing'),
    path('edit/<int:id>', views.product_edit, name='product_edit'),
    path('delete/<int:id>', views.product_delete, name='product_delete'),
    path('review/<int:id>', views.product_review, name='product_review'),
    path('bidding/<int:id>', views.product_bidding, name='product_bidding'),
]