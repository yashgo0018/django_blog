from .settings import TITLE


def globals(request):
    return {'site_title': TITLE}
