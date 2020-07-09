from pymysql import connect

class Database:
    def my_db(self):

        try:
            conn = connect(
                'localhost',
                'poulstar',
                'poulstar',
                'Shop',
            )
            cursor = conn.cursor()
        except:
            print("Error!")
        finally:
            print("connected :)")
        return conn, cursor
