f = open('test.py', 'r', encoding='utf-8')
# f.readline() 一次读取一行的内容，返回值是读取到的内容(str)

# buf = f.readline()
# print(buf)


# f.readlines() 一次读取所有行
buf = f.readlines()
print(buf)

buf = [i.strip() for i in buf]
print(buf)