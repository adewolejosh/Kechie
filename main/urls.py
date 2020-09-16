from django.urls import path
# from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # bags
    path('product/bag/', views.product_list, {'listed': 'Bag'}, name='bag'),

    # jewelry
    path('product/jewelry/', views.product_list, {'listed': 'Jewelry'}, name='jewelry'),

    # accessory
    path('product/accessory/', views.product_list, {'listed': 'Accessory'}, name='accessory'),

    # shoes
    path('product/shoe/', views.product_list, {'listed': 'Shoe'}, name='shoe'),

    # detail view
    path('product/<int:pk>/', views.product_detail, name='detail'),

    # cart
    path('add_cart/', views.update_cart, name='addCart'),
    path('my-cart/', views.cart_view, name='cart'),

    # checkout
    path('checkout/', views.proceed_to_checkout, name='checkout'),
]
