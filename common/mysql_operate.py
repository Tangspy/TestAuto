import pymysql


def mysql_operate():
    # 链接数据库，user，password，host（地址），port端口，database表名
    conn = pymysql.Connection(user='root', password='123456', host='localhost',
                              port=3306, database='ecs', charset='gbk', autocommit=True)
    cursor = conn.cursor()  # 获取游标，默认游标，元组列表，元组嵌套元组

    # 查询语句
    # select_sql = 'select goods_name,goods_id from ecs_goods where goods_id <10'
    # result = cursor.execute(select_sql)  # 执行查询语句
    # print(result)  # 查询到8调数据
    # 取出的数据是元组/元组嵌套元组
    # print(cursor.fetchone())  # fetchone取第一条数据
    # print(cursor.fetchone())  # 上面取了第一条数据，这里取第二条数据
    # print(cursor.fetchmany(3))  # fetchmany取自定义条数据
    # print(cursor.fetchall())  # fetchall取出所有数据

    # 修改语句
    # update_sql = "update ecs_goods set goods_name='索爱原装M2读卡器' where goods_id = 5"
    # result1 = cursor.execute(update_sql)  # 执行修改语句
    # print(result1)  # 影响结果条数

    # cursor = conn.cursor(pymysql.cursors.DictCursor)  # 字典游标，列表嵌套字典
    # cursor.execute("select goods_name,goods_id from ecs_goods where goods_id =5")
    # print(cursor.fetchall())

    # 参数化执行---一般用在插入insert，查询不用
    cursor.executemany("select goods_name,goods_id from ecs_goods where goods_id =%s", (1, 2, 5))
    print(cursor.fetchall())  # 用于查询只能查到最后条数据

    cursor.close()
    conn.close()
    pass


class MysqlOperate():

    params = {
        "user": "root",
        "password": "123456",
        "host": "localhost",
        "port": 3306,
        "database": "ecs",
        "charset": "gbk",
        "autocommit": True,
    }

    def get_select_all(self, sql):
        conn = pymysql.Connection(**self.params)
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as err:
            print(err)
            pass
        finally:
            cursor.close()
            conn.close()

        pass

    def get_select(self, sql):
        pass

    def dml(self, sql):
        pass

    def dml_param(self, sql, param):
        pass

    pass


if __name__ == '__main__':
    asd = MysqlOperate().get_select_all("select goods_name,goods_id from ecs_goods where goods_id =5")
    print(asd)
