import sqlite3

def connect():
    conn=sqlite3.connect("studentss.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name text, branch text, phone integer, regno integer)")
    conn.commit()
    conn.close()

def insert(name,branch,phone,regno):
    conn=sqlite3.connect("studentss.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?)",(name,branch,phone,regno))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("studentss.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM student")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="",branch="",phone="",regno=""):
    conn=sqlite3.connect("studentss.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM student WHERE name=? OR branch=? OR phone=? OR regno=?", (name,branch,phone,regno))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("studentss.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM student WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,branch,phone,regno):
    conn=sqlite3.connect("studentss.db")
    cur=conn.cursor()
    cur.execute("UPDATE student SET name=?, branch=?, phone=?, regno=? WHERE id=?",(name,branch,phone,regno,id))
    conn.commit()
    conn.close()

connect()
