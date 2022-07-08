# 1. 用只读的方式打开文件
# 2. 读取文件内容
# 3. 关闭文件
# 4. 只写方式打开新文件
# 5. 第二步读取的内容写入新文件
# 6. 关闭新文件

# 思考：
#   1. 如果文件比较大，循环读取文件
#   2. 原文件可以是txt文件，也可能是二进制文件，所以统一使用二进制文件打开

name = input('请输入要备份的文件名\n')

f = open(name, 'rb')
buf = f.read()
f.close()

# 根据原文件名找到文件的后缀和文件名  这里用到了字符串的切片方法
index = name.rfind('.')

file_name = name[:index] + '[备份]' + name[index:]
c = open(file_name, 'wb')
c.write(buf)
c.close()
