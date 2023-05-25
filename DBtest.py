import psycopg2

class DataBase:
    def __init__(self, host, database, user, password) -> None:
        self.conn = None
        self.cur = None
        connected = self.connect(host, database, user, password)
        if connected:
            self.runQuery()
    
    def connect(self, host, database, user, password):
        try:
            self.conn = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password)

            self.cur = self.conn.cursor()

            print('PostgreSQL database version:')
            self.cur.execute('SELECT version()')

            db_version = self.cur.fetchone()
            print(db_version)
            return True
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return False
    
    def runQuery(self):
        inp = ""
        while True:
            inp = input("SQL Query:\n")
            if inp == 'q':
                break
            self.cur.execute(inp)
            res = self.cur.fetchone()
            while res != None:
                print(res)
                res = self.cur.fetchone()

        self.closeConnection()
    
    def closeConnection(self):
        self.cur.close()
        self.conn.close()

if __name__ == "__main__":
    db = DataBase("localhost", "DIS_Project", "postgres", "DISProjectPass")
