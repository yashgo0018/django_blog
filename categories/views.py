from django.shortcuts import render
from django.views.generic import DetailView

from .models import Category


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category.html'
    slug_field = "name"
    slug_url_kwarg = "name"

