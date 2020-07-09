from pymysql import connect

class Connect():
    def database(self):
        try:
            conn = connect('localhost',
                           'poulstar',
                           'poulstar',
                           'test01')

            cursor = conn.cursor()
        except:
            print("error")
        finally:
            print("connect")
        return conn, cursor

c = Connect()
c.database()