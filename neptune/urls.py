"""neptune URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView, RedirectView

from rest_framework.documentation import include_docs_urls

if settings.DEBUG:  # pragma: no cover
    import debug_toolbar
    urlpatterns = [re_path(r'^__debug__/', include(debug_toolbar.urls))]
else:
    urlpatterns = []

urlpatterns += [
    path('master', RedirectView.as_view(url='master/')),
    path('master/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('docs', RedirectView.as_view(url='docs/')),
    path('docs/', include_docs_urls(title='NeptunePPA API', public=True)),
    re_path(r'^admin/?.*', TemplateView.as_view(template_name='frontend.html')),
]
