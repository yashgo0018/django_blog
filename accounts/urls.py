from django.urls import path

from .views import (DashboardView, LoginView, PostCreateView, PostUpdateView,
                    RegisterView, logout_view)

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('logout/', logout_view, name="logout"),
    path('', DashboardView.as_view(), name="dashboard"),
    path('create/post/', PostCreateView.as_view(), name="create_post"),
    path('update/<pk>/', PostUpdateView.as_view())

]
