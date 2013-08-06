# -*- coding: utf-8 -*-

from django import template
register = template.Library()

@register.filter
def m_join(list, str):
    return str.join(list)