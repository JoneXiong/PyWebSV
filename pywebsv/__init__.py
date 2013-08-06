# -*- coding: utf-8 -*-
'''
用于构建Mole系统web服务扩展
'''
from config import DJANGO_MODEL

__version__ = "0.1"

if not DJANGO_MODEL:
    import route_func