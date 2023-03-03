import pymysql

if __name__ == '__main__':
    conn = pymysql.connect(
        user='root',
        password='root',
        host='localhost',
        port=3306,
        charset='utf8',
        database='test'
    )
    cursor = conn.cursor()
    try:
        # 插入
        sql = 'insert into stu(name) values("zpan");'
        row = cursor.execute(sql)
        print(row)
        # 提交事务
        conn.commit()
    except Exception as e:
        print(e)
        # 回滚
        conn.rollback()
    cursor.close()
    conn.close()
    