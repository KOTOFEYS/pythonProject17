import sqlite3

def initiate_db():
    connection = sqlite3.connect("initiate.db")
    cursor = connection.cursor()
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
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect("initiate.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    return products