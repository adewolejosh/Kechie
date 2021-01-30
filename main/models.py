from django.db import models
from accounts.models import User


GENDERS = (
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('All', 'All'),
)

GENDER = (
    ('ALL', 'All'),
)


class Category(models.Model):
    name = models.CharField(max_length=15)
    gender = models.TextField(choices=GENDER, default=['All'])

    def __str__(self):
        return '%s' % self.name


class Product(models.Model):
    name = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genders = models.TextField(verbose_name='For Which Gender?', choices=GENDERS, default='----')
    size = models.PositiveIntegerField(blank=True, null=True, default=40)
    dprice = models.DecimalField(verbose_name='If discount, what price?', max_digits=10, decimal_places=1, blank=True, null=True)
    image = models.FileField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=2500)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        ordering = ('-id', )


class Cart(models.Model):
    customer = models.CharField(max_length=50)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.pk)

    @property
    def get_cart_total(self):
        cartItems = self.cartitem_set.all()
        total = sum([item.get_total for item in cartItems])
        return total

    @property
    def get_cart_items(self):
        cartItems = self.cartitem_set.all()
        total = sum([item.quantity for item in cartItems])
        return total


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.order.pk, self.order.customer)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    email = models.EmailField()
    phone = models.PositiveIntegerField()
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    h_o_address = models.TextField(max_length=300, verbose_name='Home/Office Address')
    o_c_address = models.TextField(max_length=300, verbose_name='Order Collection Address')
    city = models.TextField(max_length=20)
    state = models.CharField(max_length=20)
    zip = models.IntegerField(default=100200)

    created = models.DateTimeField(auto_now_add=True)
    date_ordered = models.DateField(auto_now_add=True)
    time_ordered = models.TimeField(auto_now_add=True)

    pending = models.BooleanField(default=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return '# %s - %s' % (self.pk, self.customer)


class ItemOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # order = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    # date_added = models.DateTimeField(auto_now_add=True)
    # cartProducts = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    ordering = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return '# %s - %s' % (self.ordering.pk, self.ordering.customer)

    @property
    def transaction_id(self):
        return self.ordering.pk

    @property
    def pending_status(self):
        return self.ordering.pending

    @property
    def complete_status(self):
        return self.ordering.complete

    # @property
    # def get_total(self):
    #     return self.cartProducts.get_total
