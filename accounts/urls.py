from django.urls import path

from posts.views import PostDeleteView, PostsList

from .views import (DashboardView, LoginView, PostCreateView, PostUpdateView,
                    RegisterView, logout_view)

urlpatterns = [
    # Dashboard Related Urls
    path('', DashboardView.as_view(), name="dashboard"),

    # Auth related urls
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('logout/', logout_view, name="logout"),

    # Post related urls
    path('create/post/', PostCreateView.as_view(), name="create_post"),
    path('posts/<slug>/update/', PostUpdateView.as_view(), name="edit_post"),
    path('posts/', PostsList.as_view(template_name="accounts/admin/posts.html"),
         name="list_posts"),
    path('posts/<slug>/delete/', PostDeleteView.as_view(), name="delete_post")
]
