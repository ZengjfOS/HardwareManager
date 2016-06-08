#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 1. 以下代码保存在HardwareManager项目的目录下，名称叫：setup.py；
# 2. 进度dos窗口，跳转到项目目录；
# 3. 执行：python setup.py；
# 4. 进入生成的dist目录下，双击main.exe文件，就可以执行了

# 参考文章：
#   1. py2exe使用方法
#       http://www.cnblogs.com/jans2002/archive/2006/09/30/519393.html
#   2. Py2exe打包PyQt4
#       http://www.huomo.cn/developer/article-7a92.html
#   3. ImportError: No module named sip
#       http://www.py2exe.org/index.cgi/Py2exeAndPyQt
#   4. py2exe error: MSVCP90.dll: No such file or directory
#       http://blog.csdn.net/sunny5211/article/details/6431864

from distutils.core import setup
import py2exe
import os
import sys#this allows to run it with a simple double click.

def getpwd():
    pwd = sys.path[0]
    if os.path.isfile(pwd):
        pwd = os.path.dirname(pwd)
    return pwd

sys.argv.append('py2exe')

script = [{
    "script":"main.pyw", 
    'icon_resources':[(0, getpwd()+'\logo.ico')]
    }]
py2exe_options = {
        "includes":["sip",],
        "dll_excludes":["MSVCP90.dll"],
        }
setup(windows=script,options={'py2exe':py2exe_options})

