from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from categories.views import CategoryDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('posts.urls')),
    path('categories/<name>', CategoryDetail.as_view(), name='Category_detail'),
    path('pages/', include('pages.urls')),
    path('accounts/', include('accounts.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
