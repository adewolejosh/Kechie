
from django.urls import path
# from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # bags
    path('product/bag/', views.product_list, {'listed': 'Bag'}, name='bag'),
    path('product/female-bag/', views.product_categ_list, {'listed': 'Bag', 'genders': 'Female'}, name='f-bag'),
    path('product/male-bag/', views.product_categ_list, {'listed': 'Bag', 'genders': 'Male'}, name='m-bag'),

    # jewelry
    path('product/jewelry/', views.product_list, {'listed': 'Jewelry'}, name='jewelry'),
    path('product/female-jewelry/', views.product_categ_list, {'listed': 'Jewelry', 'genders': 'Female'}, name='f-jewelry'),
    path('product/male-jewelry/', views.product_categ_list, {'listed': 'Jewelry', 'genders': 'Male'}, name='m-jewelry'),

    # accessory
    path('product/accessory/', views.product_list, {'listed': 'Accessory'}, name='accessory'),
    path('product/female-accessory/', views.product_categ_list, {'listed': 'Accessory', 'genders': 'Female'}, name='f-accessory'),
    path('product/male-accessory/', views.product_categ_list, {'listed': 'Accessory', 'genders': 'Male'}, name='m-accessory'),

    # shoes
    path('product/shoe/', views.product_list, {'listed': 'Shoe'}, name='shoe'),
    path('product/female-shoe/', views.product_categ_list, {'listed': 'Shoe', 'genders': 'Female'}, name='f-shoe'),
    path('product/male-shoe/', views.product_categ_list, {'listed': 'Shoe', 'genders': 'Male'}, name='m-shoe'),

    # detail view
    path('product/<int:pk>/', views.product_detail, name='detail'),

    # cart
    path('add_cart/', views.update_cart, name='addCart'),
    path('my-cart/', views.cart_view, name='cart'),

    # checkout
    path('checkout/', views.proceed_to_checkout, name='checkout'),
]
