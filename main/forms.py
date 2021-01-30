from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .models import Order
from django import forms


def sending_mail(email, username):
    subject = "Thanks for Registering With Kechies"
    message = render_to_string('registrationMail.html', {'username': username})
    mail = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email, 'adewole.josh.mydjangotestmail@gmail.com'],
    )
    print("sent")
    mail.send()


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        # fields = '__all__'
        # ]fields = [
        #     'customer', 'email', 'phone', 'firstName', 'lastName', 'h_o_address', 'o_c_address', 'city', 'state', 'zip',
        # ]
        exclude = ('pending', 'complete')

    # def validate_customer(self, request):
    #     return request.user
