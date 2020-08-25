# -*- encoding:utf-8 -*-
import pymysql
from scrapy.utils.project import get_project_settings  # 导入seetings配置


class DBHelper:
    """这个类也是读取settings中的配置，自行修改代码进行操作"""

    def __init__(self):
        self.settings = get_project_settings()  # 获取settings配置，设置需要的信息

        self.host = self.settings['MYSQL_HOST']
        self.port = self.settings['MYSQL_PORT']
        self.user = self.settings['MYSQL_USER']
        self.passwd = self.settings['MYSQL_PASSWD']
        self.db = self.settings['MYSQL_DBNAME']

    # 连接到mysql，不是连接到具体的数据库
    def connectMysql(self):
        conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               # db=self.db,不指定数据库名
                               charset='utf8')  # 要指定编码，否则中文可能乱码
        return conn

    # 连接到具体的数据库（settings中设置的MYSQL_DBNAME）
    def connectDatabase(self):
        conn = pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               passwd=self.passwd,
                               db=self.db,
                               charset='utf8')  # 要指定编码，否则中文可能乱码
        return conn

        # 创建数据库

    def createDatabase(self):
        """因为创建数据库直接修改settings中的配置MYSQL_DBNAME即可，所以就不要传sql语句了"""
        conn = self.connectMysql()  # 连接数据库
        sql = "create database if not exists " + self.db
        cur = conn.cursor()
        cur.execute(sql)  # 执行sql语句
        cur.close()
        conn.close()

    def execute(self, sql):
        conn = self.connectDatabase()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()  # 注意要commit
        cur.close()
        conn.close()

    def executeWithPara(self, sql, *params):
        conn = self.connectDatabase()
        cur = conn.cursor()
        cur.execute(sql, params)
        conn.commit()  # 注意要commit
        cur.close()
        conn.close()
