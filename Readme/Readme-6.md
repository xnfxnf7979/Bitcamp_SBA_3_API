"""
member

CRUD
RESful: POST, GRT, UPDATE, DELETE
SQL : insert, select, update, delete 
member: join, login, update, remove
movie : register, search, update, remove

vscode
member 폴더 만들고
class Member:
    userid: str = ''
    password: str = ''
    phone: str = ''
    register: str = ''


    def __init__(self):
        quert = """
        CREATE TABLE IF NOT EXISTS member(
            userid VARCHAR(10) PRIMARY KEY,
            password VARCHAR(10),
            phone VARCHAR(10),
            regdate DATE DEFAULT CURRENT_TIMESTAMP
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_many(self):
        data = [
            ('lee','1234','010-2222-2342'),
            ('kim','13463','010-2124-2342'),
            ('hong','19078','010-5672-2342')
        ]
        query = """
            INSERT INTO member(userid,password,phone) VALUES (?,?,?)
        """

    def fetch_one(self):
        pass
    def fetch_all(self):
        pass
    def login(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass

class StudentService:
    pass

"""

