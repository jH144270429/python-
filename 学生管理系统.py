from hashlib import sha1
import pymysql

class reglogon() :

    #验证登录界面
    def run(self):
        # 提示用户输入账号信息
        print("=============欢迎登录=============")
        user_name = input("请输入用户名：")
        passwd = input("请输入密码：")


        # 连接数据库方法一
        conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="as123", db="test")
        cursor = conn.cursor()

        sql = "select * from userinfos WHERE name=%s and passwd=%s"
        cursor.execute(sql, [user_name,passwd])
        result = cursor.fetchone()

        #验证账号密码是否正确
        while result == None:
            print("用户名或者密码错误")
            user_name = input("请重新输入用户名：")
            passwd = input("请重新输入密码：")
            sql = "select * from userinfos WHERE name=%s and passwd=%s"
            cursor.execute(sql, [user_name, passwd])
            result = cursor.fetchone()

        print("登录成功！")

        #进入系统
        user = reglogon()
        user.select()

        cursor.close()  # 关闭操作游标
        conn.close()  # 释放数据库资源

    #显示系统操作信息
    def select(self):
        while 1:
            print("=======欢迎登录学生管理系统=======")
            print("========输入1插入学生信息。=======")
            print("========输入2删除学生信息。=======")
            print("========输入3修改学生信息。=======")
            print("========输入4查询学生信息。=======")
            print("========输入0退出管理系统。=======")
            print("=================================")
            print('\n')
            order = input("请输入命令指示：")

            if order == "1":
                user = reglogon()
                order = user.add()
                #返回值为0退出
                if order == 0:
                    break

            elif order == "2":
                user = reglogon()
                order = user.delete()
                # 返回值为0退出
                if order == 0:
                    break

            elif order == "3":
                user = reglogon()
                order = user.updata()
                # 返回值为0退出
                if order == 0:
                    break

            elif order == "4":
                user = reglogon()
                order = user.look()
                # 返回值为0退出
                if order == 0:
                    break

            elif order == "0":
                break

            else:
                print("请正确输入指令！！！")

    #添加学生信息
    def add(self):
        print('\n')
        print("==========插入学生信息！=========")
        while 1:
            print('\n')
            snumber = input("请输入学生学号：")
            sname = input("请输入学号名字：")
            classes = input("请输入学生班级号：")

            # 连接数据库
            conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="as123", db="test")
            cursor = conn.cursor()
            # 创建插入sql语句
            sql = "insert into student(snumber,sname,class)VALUES(%s,%s,%s)"
            cursor.execute(sql, [snumber,sname,classes])
            conn.commit()
            cursor.close()
            conn.close()
            print('\n')
            print("学生信息插入成功！")

            #是否继续插入信息
            print('\n')
            print("输入1继续插入信息")
            print("输入0退出插入指令")
            print('\n')
            add = input("请输入命令指示：")
            if add == "0":
                break


        while 1:
            print('\n')
            print("输入1回到管理系统页面")
            print("输入0退出系统")
            print('\n')
            addchoose = input("请输入命令指示：")
            #回到系统页面
            if addchoose == "1":
                user = reglogon()
                user.select()
            elif addchoose == "0":
                return 0
            else:
                print('\n')
                print("请正确输入指令！")

    #删除学生信息
    def delete(self):
        print('\n')
        print("==========删除学生信息！=========")
        while 1:
            print('\n')
            sname = input("请输入删除学生姓名：")
            # 连接数据库
            conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="as123", db="test")
            cursor = conn.cursor()
            # 创建插入sql语句
            sql = "delete from student where sname = '%s'"
            cursor.execute(sql % (sname))
            conn.commit()
            cursor.close()
            conn.close()
            print('\n')
            print("学生信息删除成功！")

            #是否继续插入信息
            print('\n')
            print("输入1继续删除信息")
            print("输入0退出删除指令")
            print('\n')
            add = input("请输入命令指示：")
            if add == "0":
                break

        while 1:
            print('\n')
            print("输入1回到管理系统页面")
            print("输入0退出系统")
            print('\n')
            addchoose = input("请输入命令指示：")
            #回到系统页面
            if addchoose == "1":
                user = reglogon()
                user.select()
            elif addchoose == "0":
                return 0
            else:
                print('\n')
                print("请正确输入指令！")

    #修改学生信息
    def updata(self):
        print('\n')
        print("==========修改学生信息！=========")

        while 1:
            print('\n')
            sname = input("请输入需要修改学生姓名：")
            classes = input("请输入需要修改学生班级：")
            # 连接数据库
            conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="as123", db="test")
            cursor = conn.cursor()
            # 创建插入sql语句
            sql = "update student set class = '%s' where sname = '%s'"
            cursor.execute(sql % (classes,sname))
            conn.commit()
            cursor.close()
            conn.close()
            print('\n')
            print("学生信息修改成功！")

            #是否继续插入信息
            print('\n')
            print("输入1继续修改信息")
            print("输入0退出修改指令")
            print('\n')
            add = input("请输入命令指示：")
            if add == "0":
                break

        while 1:
            print('\n')
            print("输入1回到管理系统页面")
            print("输入0退出系统")
            print('\n')
            addchoose = input("请输入命令指示：")
            #回到系统页面
            if addchoose == "1":
                user = reglogon()
                user.select()
            elif addchoose == "0":
                return 0
            else:
                print('\n')
                print("请正确输入指令！")

    #查看学生信息
    def look(self):
        print('\n')
        print("==========查看学生信息！=========")

        while 1:
            print('\n')
            sname = input("请输入查找信息学生姓名：")
            # 连接数据库
            conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="as123", db="test")
            cursor = conn.cursor()
            # 创建插入sql语句
            sql = "select *from student where sname='%s'"
            cursor.execute(sql % (sname))
            data = cursor.fetchall()  # 获取结果集中剩下的所有行
            for i in data:  # 将结果显示出来
                print(i)
            conn.commit()
            cursor.close()
            conn.close()
            print('\n')
            print("学生信息查找成功！")

            #是否继续查找信息
            print('\n')
            print("输入1继续查找信息")
            print("输入0退出查找指令")
            print('\n')
            add = input("请输入命令指示：")
            if add == "0":
                break

        while 1:
            print('\n')
            print("输入1回到管理系统页面")
            print("输入0退出系统")
            print('\n')
            addchoose = input("请输入命令指示：")
            #回到系统页面
            if addchoose == "1":
                user = reglogon()
                user.select()
            elif addchoose == "0":
                return 0
            else:
                print('\n')
                print("请正确输入指令！")

def main():
    user = reglogon()
    user.run()
    print('\n')
    print("已经成功退出管理系统")

if __name__ == '__main__':
    main()
