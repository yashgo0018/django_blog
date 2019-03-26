from django.shortcuts import redirect
from django.urls import reverse


class SuperUserRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_admin:
                return super().dispatch(request, *args, **kwargs)
        return redirect(f"{reverse('login')}?next={request.path}")
