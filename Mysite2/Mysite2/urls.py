"""
Definition of urls for Mysite2.
"""

from django.conf.urls import include, url
# from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # path('admin/', admin.site.urls),
    # Examples:
    # url(r'^$', Mysite2.views.home, name='home'),
    # url(r'^Mysite2/', include('Mysite2.Mysite2.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
     url(r'^admin/', admin.site.urls),
     url (r'^blog/', include('blog.urls',  namespace='blog',app_name='blog')),
     url (r'^account/', include('account.urls',  namespace='account',app_name='account')),
]
