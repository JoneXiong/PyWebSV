# -*- coding: utf-8 -*-
##################### 系统环境设置 #######################
def set_lib_path():
    import sys
    import os
    sys.path.append('./mole_libs')
set_lib_path()

from mole import route,static_file
from mole.mole import default_app

# 加载app
import pywebsv
import demo

# 配置模板目录
from mole.const import TEMPLATE_PATH
TEMPLATE_PATH.append('./pywebsv/templates/')

# 配置静态目录
@route('/rpc_static/:file#.*#')
def rpc_media(file):
    return static_file(file, root='./pywebsv/static')

app = default_app()

# 运行服务器
from mole import run
if __name__  == "__main__":
    run(app=app,host='0.0.0.0', port=8081)