import pymysql

if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', user='root', password='root', charset='utf8', database='test', port=3306)
    cursor = conn.cursor()
    
    name = input('请输入查询姓名：')  # " or 1=1 or "
    sql = f'select * from stu where name="{name}"'
    cursor.execute(sql)
    print(cursor.fetchall())
    cursor.close()
    conn.close()
    