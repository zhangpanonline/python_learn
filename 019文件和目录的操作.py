import os


# 1. 文件重命名 os.rename(原路径，新路径)
# os.rename('test.py', 'test.txt')


# 2. 删除文件 os.remove(路径)
# os.remove('test.txt')


# 3. 创建目录 os.mkdir(目录路径)
# os.mkdir('file')
# os.mkdir('file/a')


# 4. 删除空目录
# os.rmdir('file')


# 5. 获取当前所在目录 os.getcwd()  c = current w = working d = directory
# print(os.getcwd())


# 6. 修改当前所在目录 os.chdir(路径)
# os.chdir('file')
# print(os.getcwd())


# 7. 获取指定目录中的内容,默认当前目录 os.listdir()
# print(os.listdir())
