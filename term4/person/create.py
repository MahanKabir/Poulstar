from term4.person.connect import Database
class Create:
    def __init__(self, name, family, age, phone):
        self.name = name
        self.family = family
        self.age = age
        self.phone = phone
    def create_data(self):
        try:
            conn, cursor = Database().my_db()
            query = "INSERT INTO user(name, family, age, phone) VALUES(%s, %s, %s, %s)"
            data = (self.name, self.family, self.age, self.phone)
            cursor.execute(query, data)
            conn.commit()

        except:
            print("sending error!")
        finally:
            print("Sent data to your database.")

insert = Create("kamyar", "HS", "15", "0919")
insert.create_data()