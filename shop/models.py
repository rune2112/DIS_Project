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
    
def select_user(uid):
    print(f"SELECT USER, ID: {uid}")
    cur = conn.cursor()
    sql = """
    SELECT * FROM users
    WHERE username = %s
    """
    cur.execute(sql, (uid,))
    result = cur.fetchone()
    print(f"QUERY RESULT: {result}")
    user = User(result) if cur.rowcount > 0 else None
    cur.close()
    return user

def search():
    form = SearchForm()
    if form.validate_on_submit():
        company = form.company.data
        product = form.product.data
        typename = form.typename.data
        inches = form.inches.data
        resolution = form.resolution.data
        cpu = form.cpu.data
        ram = form.ram.data
        memory = form.memory.data
        gpu = form.gpu.data
        opsys = form.opsys.data
        weight = form.weight.data
        price_euros = form.price_euros.data
        res = search_for_laptop(company, product, typename, inches, resolution, cpu, ram, memory, gpu, opsys, weight, price_euros)
        return render_template('search.html', title="Search", form=form, results=res)
    else:
        return render_template('search.html', title="Search", form=form, results=None)()
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

def sell_laptop(company, product, typename, inches, resolution, cpu, ram, memory, gpu, opsys, weight, price_euros, current_user):

    cur = conn.cursor()
    getmax_sql = """
    SELECT MAX(l_id) FROM laptops;
    """
    cur.execute(getmax_sql, ())
    max_id = cur.fetchone()[0]
    userN = current_user[1]
    print(f"{userN} is trying to sell a laptop")
    sql = """
    INSERT INTO
    laptops(l_id, company, product, typename, inches, resolution, cpu, ram, memory, gpu, opsys, weight, price_euros, username)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cur.execute(sql, (max_id + 1, company, product, typename, inches, resolution, cpu, ram, memory, gpu, opsys, weight, price_euros, userN))
    conn.commit()
    cur.close()


def get_laptops_from_user(current_user):
    cur = conn.cursor()
    userN = current_user[1]
    print(f"PROFILE: {userN}")
    print(f"{type(userN)}")
    sql = """
    SELECT * FROM laptops
    WHERE username = %s;
    """
    cur.execute(sql, (userN,))
    res = cur.fetchall()
    cur.close()
    return res