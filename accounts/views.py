from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm, sending_mail


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        sending_mail(
            email=str(form.cleaned_data['email']),
            username=str(form.cleaned_data['username']),
        )
        return super(SignUpView, self).form_valid(form)


@login_required
def profile(request):
    User = request.user
    template_name = 'profile.html'
    context = {
        'User': User,
    }
    return render(request, template_name, context)
