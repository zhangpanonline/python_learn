# 二进制文件，只能使用二进制的方式打开，例如音频、视频、图片等
# rb wb ab
# 注意点：不能指定 encoding 参数

f = open('test.py', 'wb')
f.write('你哈'.encode())
f.close()

f1 = open('test.py', 'rb')
buf = f1.read()
print(buf.decode())
f1.close()
