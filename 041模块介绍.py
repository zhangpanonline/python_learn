"""
方法一 import 模块名
使用：模块名.功能

方法二 from 模块名 import 功能名1，功能名2，...
使用：功能名
注意点：如果存在同名的方法名，则会被覆盖

方法三 from 模块名 import * # 将模块中所有的功能进行导入
使用：功能名

as 起别名
import module as m1
import module from func as fn

__all__ 变量，可以在每个代码文件（模块中）定义，类型是元组、列表
作用：影响 from 模块名 import * 导入行为
1. 如果没有定义 __all__ 变量，模块中的所有功能，都可以被导入
2. 如果定义  __all__ 变量，只能导入变量中定义的内容
"""
