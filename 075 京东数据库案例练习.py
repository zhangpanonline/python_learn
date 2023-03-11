"""
需求：
1. 查询所有商品信息
    query_all_info
2. 查询所有包含商品的分类 
    query_goods_cates
3. 添加新商品分类
    add_new_cate
4. 将所有商品价格加1000
    update_price
5. 将所有笔记本的分类改为超极本
    modify_goods_cate
6. 根据id查询商品信息
    query_goods_by_id
7. 根据id查询商品信息安全方式（解决SQL注入）
8. 退出系统
"""
import pymysql


class JDServer(object):
    # 连接对象一般写在 init 方法中
    # 游标一般不作为实例属性，一般在方法中使用的时候创建，方法中使用完成之后关闭
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='jing_dong', charset='utf8')

    @staticmethod
    def show_menu():
        print('1. 查询所有商品信息')
        print('2. 查询所有包含商品的分类')
        print('3. 添加新商品分类')
        print('4. 将所有商品价格加1000')
        print('5. 将所有笔记本的分类改为超极本')
        print('6. 根据id查询商品信息')
        print('7. 根据id查询商品信息安全方式（解决SQL注入）')
        print('8. 退出系统')
        
    def __del__(self):
        self.conn.close()
        
    def start(self):
        while True:
            self.show_menu()
            opt = input('请输入要进行的操作：')
            if opt == '1':
                self.query_all_info()
            elif opt == '2':
                self.query_goods_cates()
            elif opt == '3':
                self.add_new_cate()
            elif opt == '4':
                self.update_price()
            elif opt == '5':
                self.modify_goods_cate()
            elif opt == '6':
                self.query_goods_by_id()
            elif opt == '7':
                self.query_goods_by_id_safe()
            elif opt == '8':
                print("欢迎下次使用本系统。")
                break
            else:
                print('输入有误，请再次输入：')
                continue
            input('\n 回车键继续')
       
    def query_all_info(self):
        cursor = self.conn.cursor()
        sql = "select * from goods" \
              " left join goods_cates on goods.cate_id = goods_cates.id" \
              " left join goods_brands on goods.brand_id = goods_brands.id;"
        row = cursor.execute(sql)
        print(f'查询到{row}条数据：')
        for row in cursor.fetchall():
            print(row)
        cursor.close()
    
    def query_goods_cates(self):
        cursor = self.conn.cursor()
        sql = "select * from goods_cates where id in (select distinct cate_id from goods);"
        rows = cursor.execute(sql)
        print(f'查询到{rows}条数据:')
        for row in cursor.fetchall():
            print(row)
        cursor.close()
    
    def add_new_cate(self):
        sql = "insert into goods_cates(name) values(%s);"
        name = input('请输入新的商品分类：')
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, [name])
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        cursor.close()
    
    def update_price(self):
        sql = 'update goods set price=price+%s;'
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql, [1000])
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        cursor.close()
    
    def modify_goods_cate(self):
        sql = """"""
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        cursor.close()
    
    def query_goods_by_id(self):
        good_id = input('请输入商品ID：\n')
        cursor = self.conn.cursor()
        sql = f"select * from goods where id = {good_id};"
        rows = cursor.execute(sql)
        print(f'查询到{rows}条数据：')
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        
    def query_goods_by_id_safe(self):
        good_id = input('请输入商品ID：\n')
        cursor = self.conn.cursor()
        sql = "select * from goods where id = %s;"
        rows = cursor.execute(sql, (good_id,))
        print(f'查询到{rows}条数据：')
        for row in cursor.fetchall():
            print(row)
        cursor.close()
    
    
if __name__ == '__main__':
    jd = JDServer()
    jd.start()
    