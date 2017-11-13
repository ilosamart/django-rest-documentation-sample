"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

from rest_framework_swagger.views import get_swagger_view

from snippets.urls import router as snippet_router_v1

API_PREFIX = r'^api/v(?P<version>[0-9]+\.[0-9]+)'
# API_PREFIX = r'^api'

MY_API_TITLE = 'My API title'

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'%s/' % API_PREFIX, include('drf_openapi.urls')),
    url(r'%s/docs/' % API_PREFIX, include_docs_urls(title=MY_API_TITLE)),
    url(r'%s/swagger/' % API_PREFIX, include_docs_urls(title=MY_API_TITLE)),
    url(r'%s/snippets/' % API_PREFIX, include(snippet_router_v1.urls, namespace='snippets')),
]
