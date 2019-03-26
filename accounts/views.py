from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.views.generic import CreateView, FormView, TemplateView, UpdateView

from posts.forms import PostForm
from posts.models import Post

from .forms import LoginForm, RegisterForm
from .mixins import SuperUserRequiredMixin


class RegisterView(FormView):
    template_name = "accounts/register.html"
    success_url = "/accounts/login"
    form_class = RegisterForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = "accounts/login.html"
    success_url = "/"
    form_class = LoginForm

    def get_success_url(self):
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        return super().get_success_url()

    def form_valid(self, form):
        login(self.request, form.cleaned_data["user_obj"])
        return super().form_valid(form)


def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect("/")


class DashboardView(SuperUserRequiredMixin, TemplateView):
    template_name = "accounts/admin/dashboard.html"


class PostCreateView(SuperUserRequiredMixin, CreateView):
    template_name = "accounts/admin/create/post.html"
    model = Post
    queryset = Post.objects.all()
    form_class = PostForm

    def form_valid(self, form):
        form.cleaned_data["author"] = self.request.user
        return super().form_valid(form)


class PostUpdateView(SuperUserRequiredMixin, UpdateView):
    template_name = "accounts/admin/create/post.html"
    model = Post
    queryset = Post.objects.all()
    form_class = PostForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
