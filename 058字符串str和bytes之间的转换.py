my_str = '中国'
print(type(my_str), my_str)

str_utf8 = my_str.encode('utf-8')
print(type(str_utf8), str_utf8)

str_gbk = my_str.encode('gbk')
print(type(str_gbk), str_gbk)

print(str_utf8.decode('utf-8'), str_gbk.decode('gbk'))

