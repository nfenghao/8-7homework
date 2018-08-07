
from django.conf.urls import url, include
from django.contrib import admin
from api import urls
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/(?P<version>\w+)/', include(urls)),
    url(r'', include('app01.urls')),
]
