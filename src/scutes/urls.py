"""
URL configuration for scutes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpRequest
from django.urls import path, include, re_path

from processing.views import (
    BatchList,
    batch_convert_and_export,
    Dashboard,
    FinalizeBatchView,
    Index,
    ItemListView,
    ItemUpdateView,
    protected_media,
)

handler500 = 'processing.views.error_500'

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('batchlist/', BatchList.as_view(), name='batchlist'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('', Index.as_view(), name='index'),
    path('itemlist/<int:batch>/', ItemListView.as_view(), name='itemlistview'),
    path('finalizebatch/<int:pk>/', FinalizeBatchView.as_view(), name='finalizebatchview'),
    path('batch_convert_and_export/', batch_convert_and_export, name='batch_convert_and_export'),
    path('itemview/<int:pk>/', ItemUpdateView.as_view(), name='itemupdateview'),
    path('ckeditor5/', include('django_ckeditor_5.urls')),
    path('media/<directory>/<filename>', protected_media),
    re_path(r'saml2/', include('djangosaml2.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

htmx_urlpatterns = []

urlpatterns += htmx_urlpatterns


def get_navigation_links(request: HttpRequest):
    if request.user.is_authenticated:
        authenticated_links = {
            'dashboard': 'Dashboard',
            'batchlist': 'Batch List',
            '': f'Logged in as {request.user.username}',
            'saml2_logout': 'Log Out',
        }
        if request.user.is_superuser:
            superuser_links = {
                'admin:index': 'Admin',
            }
        else:
            superuser_links = {}
        links = {**superuser_links, **authenticated_links}
        return links
    else:
        return {'saml2_login': 'Log In'}
