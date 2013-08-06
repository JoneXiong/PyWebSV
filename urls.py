import os

from django.conf.urls.defaults import *
import demo
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^wstest/', include('wstest.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
    (r'^rpc/', include('pywebsv.django_urls')),
    url(r'^rpc_static/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.join(os.path.dirname(__file__),
        'pywebsv/static').replace('\\','/')
        },name="rpc_static"),
)
