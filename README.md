=======

A webservice tool for Python (Django or Mole)

概述
=======

一个在python (Mole或Django) 环境下快速构建 webservice 的工具库,使用了第三方库Ladon。
主要为了方便快速的将我们的Python函数发布成webservice或者RPC接口

特性
=======

1. 同时提供 SOAP 和 JSON 的支持，提供完善的在线接口描述文档界面
2. 前端即可通过JS来调用,打开调试模式即可在线在web界面调用接口方法
3. 提供soap调试demo示例和调试工具(详见界面链接)

使用
=======

Mole 环境下
1. pywebsv/config.py里
   DJANGO_MODEL = False
2. python mole_run.py
3. 访问http://127.0.0.1:8081/rpc/

Django 环境下

一 直接运行

1. pywebsv/config.py里
   DJANGO_MODEL = True
2. python django_run.py runserver 0.0.0.0:8081
3. 访问http://127.0.0.1:8081/rpc/

二 集成到已有django系统里

1. pywebsv/config.py里
   DJANGO_MODEL = True
2. settings.py中:
   INSTALLED_APPS 加入pywebsv模块
   TEMPLATE_DIRS 加入 pywebsv/templates
3. urls.py中加入两个url配置
    (r'^rpc/', include('pywebsv.django_urls'))
    url(r'^rpc_static/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.join(os.path.dirname(__file__),'pywebsv/static').replace('\\','/')},name="rpc_static")
注意:
内置的几个demo在demo.py定义，请确保系统运行时加载自己定义的webservice代码(如import demo.py)
在django环境下请注释掉CsrfViewMiddleware中间件
