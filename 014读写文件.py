# 1. 打开文件，是文件从硬盘中存到内存中
# open(file, mode='r', encoding)
# encoding 文件的编码格式，常见的编码格式：gbk、utf-8
# 返回值，文件对象，后续所有的文件操作，都需要这个文件对象执行
f = open('test.py', 'a', encoding='utf-8')
# 2. 读文件  文件对象.read()
# buf = f.read()
# print(buf)
# 3. 写文件  文件对象.write(写入文件的内容)
f.write('hellow\n')
f.write('world\n')
f.write('你好')
# 4. 关闭文件  文件.close()，将内存中的文件同步到硬盘中
f.close()

