# 1. 导包
import pymysql

if __name__ == '__main__':
    # 2. 创建连接对象
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='test',
        port=3306,
        charset='utf8')
    # 3. 创建游标对象
    cursor = conn.cursor()
    # 4. 执行 SQL 语句
    # 4.1 书写 SQL
    sql = 'select * from stu;'
    # 4.2 执行 SQL
    # 返回值是影响的行数
    # 对于查询操作来说，查询出来的数据保存在游标对象中
    row = cursor.execute(sql)
    print(f'{row} rows in set')
    # 获取查询结果，对于游标中保存的数据，只能获取一次，获取之后就不能再次获取了
    # print(cursor.fetchone())  # 获取一条查询结果
    print(cursor.fetchall())  # 获取所有的数据
    # cursor.fetchmany()
    # 5. 关闭游标
    cursor.close()
    # 6. 关闭连接对象
    conn.close()
    
    