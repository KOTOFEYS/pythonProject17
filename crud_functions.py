import sqlite3

def initiate_db():
    connection = sqlite3.connect("initiate.db")
    connection = sqlite3.connect("Users.db")
    cursor = connection.cursor()
    cursor1 = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER, 
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    """)
    id = ["1", "2", "3", "4"]
    title = ["Циклоферон", "Ренни", "Панадол", "Доксиламин"]
    description = ["От гриппа","От изжоги", "Болеутоляющее", "От диареи"]
    price = ["100", "200", "300", "400"]
    cursor.execute("INSERT OR REPLACE INTO Products(id, title, description, price) VALUES (?, ?, ?, ?)",
                   (f"{id[0]}", f"Название:{title[0]}", f"Описание:{description[0]}", f"Цена:{price[0]}"))
    cursor.execute("INSERT OR REPLACE INTO Products(id, title, description, price) VALUES (?, ?, ?, ?)",
                   (f"{id[1]}", f"Название:{title[1]}", f"Описание:{description[1]}", f"Цена:{price[1]}"))
    cursor.execute("INSERT OR REPLACE INTO Products(id, title, description, price) VALUES (?, ?, ?, ?)",
                   (f"{id[2]}", f"Название:{title[2]}", f"Описание:{description[2]}", f"Цена:{price[2]}"))
    cursor.execute("INSERT OR REPLACE INTO Products(id, title, description, price) VALUES (?, ?, ?, ?)",
                       (f"{id[3]}", f"Название:{title[3]}", f"Описание:{description[3]}", f"Цена:{price[3]}"))
    cursor1.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY, 
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    """)
    connection.commit()

def get_all_products():
    connection = sqlite3.connect("initiate.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.commit()
    return products

def add_user(username, email, age):
    connection = sqlite3.connect("Users.db")
    cursor1 = connection.cursor()
    cursor1.execute(f'''INSERT INTO Users (username, email, age, balance)VALUES (?,?,?,?)''',
                    (username, email, age, 1000))
    connection.commit()


def is_included(username):
    connection = sqlite3.connect("Users.db")
    cursor1 = connection.cursor()
    cursor1.execute("SELECT * FROM Users WHERE username = ?", (username,))
    user_id = cursor1.fetchone()
    if user_id is None:
        return False
    else:
        return True




