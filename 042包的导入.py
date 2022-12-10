"""
包：功能相近或者相似的模块放在一个目录中，并在目录中定义一个 __init__.py 文件
"""
# 方法一   import 包名.模块名
# import my_package.module1
# import my_package.module2 as mm2
# my_package.module1.fn()
# mm2.fn()

# 方法二   from 包名.模块名 import 功能名
# from my_package.module1 import fn 
# from my_package.module2 import fn as f1
# # from my_package.module2 import *  # 引入模块下所有功能
# fn()
# f1()

# 方法三   from 包名 import *    # 导入的是 __init__.py 中的内容
from my_package import *
fn()
