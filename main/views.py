import random
import uuid

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
import json

from django.views import View

from .models import Product, Cart, CartItem

###
# todo: check if cookie is allowed
# todo: checkout logic, payment logic
# todo: Copy the remove functionality
# todo: if allowed, create a function or method to create one for 'device' on the views |_COMPLETED_|
# todo: set customer to the created device or request.user |_COMPLETED_|
###


class TestCookie(View):
    def test_cookie(self):
        pass

    @staticmethod
    def create_cookie(request):
        if 'device' in request.COOKIES:
            return request.COOKIES['device']
        else:
            cs = HttpResponse('Setting Cookie')
            return cs.set_cookie('device', uuid.uuid4())


def home(request):
    template_name = 'home.html'

    User = request.user
    if User.is_authenticated:
        customer = request.user
    else:
        customer = str(TestCookie.create_cookie(request))

    cartItem, created = Cart.objects.get_or_create(customer=customer, complete=False)
    cartItems = cartItem.get_cart_items

    context = {
        'cartItems': cartItems,
    }
    return render(request, template_name, context)


def product_list(request, listed='', ):
    template_name = 'list.html'

    User = request.user
    if User.is_authenticated:
        customer = request.user
    else:
        customer = str(TestCookie.create_cookie(request))

    cartItem, created = Cart.objects.get_or_create(customer=customer, complete=False)
    cartItems = cartItem.get_cart_items

    context = {
        'product': Product.objects.filter(category__name=listed),
        'category': listed,
        'cartItems': cartItems,
    }
    return render(request, template_name, context)


# def product_detail(request, pk):
#     template_name = 'detail.html'
#     details = get_object_or_404(Product, pk=pk)
#     context = {
#         'product': details,
#     }
#     return render(request, template_name, context)
# def product_detail(request, pk):
#     template_name = 'detail.html'
#
#     if request.method == 'GET':
#         details = get_object_or_404(Product, pk=pk)
#         form = ProductAddToCartForm(request.GET)
#         context = {
#             'product': details,
#             'form': form,
#         }
#         return render(request, template_name, context)
#
#     if request.method == 'POST':
#         form = ProductAddToCartForm(request.POST)
#         if form.is_valid():
#             quantity = form.cleaned_data['quantity']
#             product_id = form.cleaned_data['product_id']
#             form.save()
#             success_url = reverse_lazy('cart')
#
#             return redirect(success_url)
#
#         # context = {
#         #     'product': details,
#         # }
#         # return render(request, template_name, context)


# def product_detail(request, pk):
#     template_name = 'detail.html'
#     details = get_object_or_404(Product, pk=pk)
#
#     if request.method == 'GET':
#         form = ProductAddToCartForm(request.GET)
#         context = {
#             'product': details,
#             'form': form,
#         }
#         return render(request, template_name, context)
#
#     if request.method == 'POST':
#         form = ProductAddToCartForm(request.POST)
#         if form.is_valid():
#             pk = form.cleaned_data['product.id']
#             quantity = form.cleaned_data['quantity']
#             product_details = get_object_or_404(Product, pk=pk)
#             cart_product = cart.get_cart_items()
#             product_in_cart = False
#             for cart_item in cart_product:
#                 if cart_item.product.id == product_details.id:
#                     cart_item.augment_quantity(quantity)
#                     product_in_cart = True
#             if not product_in_cart:
#                 ci = CartItem()
#                 ci.product = product_details
#                 ci.quantity = quantity
#                 ci.cart_id = cart.cart_id
#                 ci.save()
#
#             if request.session.test_cookie_worked():
#                 request.session.delete_test_cookie()
#
#             success_url = reverse_lazy('cart')
#             messages.success(request, "Product added to cart")
#             return redirect(to=success_url)
#
#         else:
#             form = ProductAddToCartForm(request.GET)
#             messages.error(request, "An error occurred. Sorry, try again!")
#             context = {
#                 'product': details,
#                 'form': form,
#             }₦
#             return render(request, template_name, context)
#
#     return render(request, template_name)
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'detail.html'
#     context_object_name = 'product'
#
#     # def post(self, request, *args, **kwargs):
#     #     form = ProductAddToCartForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #         return reverse_lazy('cart')
#     #     else:
#     #         form = ProductAddToCartForm(request.GET)
#     #         return render(request, self.template_name, {'form': form})

def product_detail(request, pk):
    template_name = 'detail.html'
    details = get_object_or_404(Product, pk=pk)
    # pro = Product.objects.filter(category__name=details.category.name)

    User = request.user
    if User.is_authenticated:
        customer = request.user
    else:
        customer = str(TestCookie.create_cookie(request))

    cartItem, created = Cart.objects.get_or_create(customer=customer, complete=False)
    cartItems = cartItem.get_cart_items

    if request.method == 'GET':
        context = {
            'product': details,
            'cartItems': cartItems,
            # 'pro': pro,
            # 'pro': Product.objects.filter(id__lte=3),
        }
        return render(request, template_name, context)

    return render(request, template_name)


def update_cart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    User = request.user
    if User.is_authenticated:
        customer = str(request.user)
    else:
        customer = str(TestCookie.create_cookie(request))

    product = Product.objects.get(id=productId)
    cart, created = Cart.objects.get_or_create(customer=customer, complete=False)
    cartItems, created = CartItem.objects.get_or_create(order=cart, product=product)

    if action == 'add':
        cartItems.quantity = cartItems.quantity + 1
    elif action == 'remove':
        cartItems.quantity = cartItems.quantity - 1

    cartItems.save()

    if cartItems.quantity <= 0:
        cartItems.delete()

    return JsonResponse('Item was added', safe=False)


def cart_view(request):
    template_name = "cart.html"
    User = request.user
    if User.is_authenticated:
        customer = request.user
    else:
        customer = str(TestCookie.create_cookie(request))

    cartItem, created = Cart.objects.get_or_create(customer=customer, complete=False)
    cartItems = cartItem.get_cart_items
    items = cartItem.cartitem_set.all()
    total = cartItem.get_cart_total

    context = {'items': items, 'cartItem': cartItem, 'cartItems': cartItems, 'total': total, }
    return render(request, template_name, context)


@login_required
def proceed_to_checkout(request):
    template_name = 'checkout.html'

    customer_user = request.user
    cartItem1, created = Cart.objects.get_or_create(customer=customer_user, complete=False)
    items1 = cartItem1.cartitem_set.all()

    customer_device = str(TestCookie.create_cookie(request))
    cartItem2, created = Cart.objects.get_or_create(customer=customer_device, complete=False)
    items2 = cartItem2.cartitem_set.all()

    if request.method == 'GET':
        if len(items2) > len(items1):
            customer = customer_device

        elif len(items2) == len(items1):
            customer = customer_device or customer_user

        else:
            customer = request.user

        cartItem, created = Cart.objects.get_or_create(customer=customer, complete=False)
        cartItems = cartItem.get_cart_items
        items = cartItem.cartitem_set.all()
        total = cartItem.get_cart_total

        context = {
            'items': items,
            'cartItem': cartItem,
            'cartItems': cartItems,
            'total': total,
        }

        return render(request, template_name, context)

    return render(request, template_name, )
