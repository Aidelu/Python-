# 代码->模块->包
# 每一个包目录下面都会有一个__init__.py的文件，
# 这个文件是必须存在的，否则，Python就把这个目录当成普通目录，
# 而不是一个包。__init__.py可以是空文件，也可以有Python代码，
# 因为__init__.py本身就是一个模块，而它的模块名就是包名。

#模块的代码模板:

#!/usr/bin/env python3                          # 可以让这个hello.py文件直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-                         # 表示.py文件本身使用标准UTF-8编码

' a test module '                               # 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'LUYUJIA'                          # 使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名

import sys                                      # 导入模块

def test():
    args = sys.argv                             # argv变量用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 当我们在命令行运行hello模块文件时，
# Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试
if __name__=='__main__':
    test()

#通过_前缀来实现私有变量和私有函数
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)