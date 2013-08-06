# -*- coding: utf-8 -*-

from django.template import add_to_builtins
add_to_builtins('pywebsv.django_tags')

def getJSResponse(content=None):
        '''
        返回 js response
        '''
        response = HttpResponse(mimetype="application/javascript")
        response["Pragma"]="no-cache"
        response["Cache-Control"]="no-store"
        response["Content-Type"]="application/javascript; charset=utf-8"
        if content:
                if type(content)==type({}):
                        from django.utils import simplejson
                        content=simplejson.dumps(content)
                response.write(content)
        return response