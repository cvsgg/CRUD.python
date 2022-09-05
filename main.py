import sqlite3 as lite

#CONNECT WITH DB
con = lite.connect('bank.db')

#CRUD
#C - CREATE - INSERT DATA
def insere_dados(i):
    with con:
        cur = con.cursor()
        insert = "INSERT INTO users(name, age, category) VALUES (?,?,?)"
        cur.execute(insert, i)

#R - READ
def mostra_dados():
    read_data = []
    with con:
        cur = con.cursor()
        insert = "SELECT * FROM users"
        cur.execute(insert)

        rows = cur.fetchall()
        for row in rows:
            read_data.append(row)
    return read_data

#U - UPDATE
def atualiza_dados(i):
    with con:
        cur = con.cursor()
        insert = "UPDATE users SET name=?, age=?, category=? WHERE id=?"
        cur.execute(insert, i)

#D - DELETE
def deleta_dados(i):
    with con:
        cur = con.cursor()
        insert = "DELETE FROM users WHERE id=?"
        cur.execute(insert,i)

#FIND
def encontra_dados(id):
    find_data = []
    with con:
        cur = con.cursor()
        insert = "SELECT * FROM users WHERE id=?"
        cur.execute(insert,id)

        rows = cur.fetchall()
        for row in rows:
            find_data.append(row)