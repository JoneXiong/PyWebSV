# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from route_func import ServiceList_django, NamedSoapView_django, NamedServiceView_django

urlpatterns=patterns('webservice',
    (r'^$',ServiceList_django),
    (r'^(?P<service_name>[^/]*)/$',NamedSoapView_django),
    (r'^(?P<service_name>[^/]*)/(?P<interface>[^/]*)',NamedServiceView_django),
    (r'^(?P<service_name>[^/]*)/(?P<interface>[^/]*)/description',NamedServiceView_django),
)