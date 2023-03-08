import pymysql

if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', user='root', password='root', charset='utf8', database='test', port=3306)
    cursor = conn.cursor()
    
    name = input('请输入查询姓名：')  # " or 1=1 or "
    # sql = f'select * from stu where name="{name}"'
    # cursor.execute(sql)
    # SQL 注入问题的解决，不适用字符串拼接，使用 SQL 参数化， execute 方法的参数
    sql = 'select * from stu where name=%s'
    # cursor.execute(sql, (name,))
    cursor.execute(sql, [name])
    print(cursor.fetchall())
    cursor.close()
    conn.close()
    