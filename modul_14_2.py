import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
               ("User1", "example1@gmail.com", "10", "1000"))
for i in range(2,11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
                   (f"User{i}", f"example{i}@gmail.com", f"{i*10}", "1000"))

for i in range(1,11,2):
    cursor.execute("UPDATE Users SET balance = ? WHERE id % 2 != 0", (500,))

for i in range (1,11,3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (f"{i}",))

cursor.execute("SELECT * FROM Users")
users = cursor.fetchall()

for user in users:
    if user[3] != 60:
        print(f"Имя:{user[1]}| Почта:{user[2]} | Возраст:{user[3]} | Баланс:{user[4]}")

cursor.execute("DELETE FROM Users WHERE id = ?", (f"{6}",))
cursor.execute("SELECT COUNT(*) FROM Users")
quantity_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
sum_total = cursor.fetchone()[0]

cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]
print(avg_balance)




connection.commit()
connection.close()
