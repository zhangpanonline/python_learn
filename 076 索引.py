import pymysql


if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='test', charset='utf8')
    cursor = conn.cursor()
    
    sql = 'insert into test values(%s);'
    try:
        for i in range(100_000):
            buf = 'test_' + str(i)
            cursor.execute(sql, [buf])
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    print('添加成功！')
    cursor.close()
    conn.close()
    