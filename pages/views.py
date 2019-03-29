from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from blog.settings import EMAIL_HOST_USER

from .forms import ContactForm


class ContactView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form: ContactForm):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')
        send_mail(subject, message, EMAIL_HOST_USER, [EMAIL_HOST_USER])
        return super().form_valid(form)


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class PolicyPageView(TemplateView):
    template_name = "pages/policy.html"
