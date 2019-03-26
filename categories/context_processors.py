from .models import Category


def tags(request):
    return {'tags': Category.objects.all()}
