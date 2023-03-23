import re

# re.match() 从头部开始匹配，匹配成功返回对象，匹配失败返回 None
# res = re.match('0\d{2}-\d{8}', '010-12387897')
# re.search() 从任意位置匹配
# res = re.search('0\d{2}-\d{8}', '_010-12387897')

# 匹配邮箱
# res = re.match("(.*)@(163|qq|sina)\.com", "qq@163.com")

# 引用分组 \num
# 匹配 HTML 双标签，方法一：
res = re.match("<([a-zA-Z]+)>.*</\\1>", "<html>hello </html>")
# 匹配 HTML 双标签，方法二，使用原生字符串：
res = re.match(r"<([a-zA-Z]+)>.*</\1>", "<html>hello </html>")
# 匹配 HTML 双标签，方法三，给引用起名字：
res = re.match("<(?P<tag>[a-zA-Z]+)>.*</(?P=tag)>", "<html>hello </html>")

if res:
    print(res.group())
    print(res.group(1))
    # print(res.group(2))
else:
    print('匹配失败')





