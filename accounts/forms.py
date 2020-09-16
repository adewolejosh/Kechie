from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from .models import User


def sending_mail(email, username):
    subject = 'Thanks for Registering With Kechies'
    message = render_to_string('registrationMail.html', {'username': username})
    mail = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email, 'adewole.josh.mydjangotestmail@gmail.com'],
    )
    print("sent")
    mail.send()


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', )
