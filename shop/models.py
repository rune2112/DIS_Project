from flask_login import UserMixin
from shop import conn, login_manager
from psycopg2 import sql

@login_manager.user_loader
def load_user(user_id):
    print(f"USER_ID: {user_id}")
    cur = conn.cursor()

    schema = 'users'
    id = 'u_id'

    user_sql = sql.SQL("""
    SELECT * FROM {}
    WHERE {} = %s
    """).format(sql.Identifier(schema),  sql.Identifier(id))

    cur.execute(user_sql, (int(user_id),))
    if cur.rowcount > 0:
        return User(cur.fetchone())
    else:
        return None




class User(tuple, UserMixin):
    def __init__(self, userData) -> None:
        self.id = userData[0]
        self.username = userData[1]
        self.password = userData[2]
    
    def get_id(self):
        return self.id
    



def select_user(id):
    print(f"SELECT USER, ID: {id}")
    cur = conn.cursor()
    sql = """
    SELECT * FROM users
    WHERE username = %s
    """
    cur.execute(sql, (id,))
    result = cur.fetchone()
    print(f"QUERY RESULT: {result}")
    user = User(result) if cur.rowcount > 0 else None
    cur.close()
    return user

def insert_user(name, password):
    cur = conn.cursor()
    sql = """
    INSERT INTO users(username, userpassword)
    VALUES (%s, %s)
    """
    cur.execute(sql, (name, password))
    # Husk commit() for INSERT og UPDATE, men ikke til SELECT!
    conn.commit()
    cur.close()

def search_for_laptop(company, product, typename, inches, resolution, cpu, ram, memory, gpu, opsys, weight, price_euros):
    cur = conn.cursor()
    args = [company, product, typename, inches, resolution, cpu, ram, memory, gpu, opsys, weight, price_euros]
    usedArgs = []
    columns = ["company", "product", "typename", "inches", "resolution", "cpu", "ram", "memory", "gpu", "opsys", "weight", "price_euros"]
    formatArr = []
    sql = """
    SELECT * FROM laptops
    WHERE 
    """
    for i in range(len(args)):
        if len(args[i]) > 0:
            sql += columns[i] + " = %s AND "
            formatArr.append(i)
    sql = sql[:-5] #Removing the last " AND "
    for i in formatArr:
        usedArgs.append(args[i])
    cur.execute(sql, (usedArgs))
    result = cur.fetchall()
    return result