from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsList.as_view(), name="posts"),
    path('post/<slug>', PostDetail.as_view(), name="Post_detail"),
    path('comment-handler/', CommentHandler.as_view())
]
