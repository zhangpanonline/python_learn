f = open('test.py', 'r', encoding='utf-8')
while True:
    buf = f.readline()
    if buf:
        print(buf, end='')
    else:
        # 文件读完
        break;

f.close()

f = open('test.py', 'r', encoding='utf-8')
while True:
    buf = f.read(5)
    if buf:
        print(buf, end='')
    else:
        break;
        
f = open('test.py', 'r', encoding='utf-8')
