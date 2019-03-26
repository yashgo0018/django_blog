from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, View

from .models import Post, Comment


class PostsList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts.html'
    paginate_by = 8


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'


class CommentHandler(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        comment = request.GET.get("comment")
        post_id = request.GET.get("post")
        post = Post.objects.filter(id=post_id).first()
        comment_obj = Comment(content=comment, author=request.user, post=post)
        comment_obj.save()
        return redirect(post.get_absolute_url())
