import sqlite3

conn = sqlite3.connect('sample.db')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE programming(Language VARCHAR, Version REAL, Skill TEXT)")

def enter_data():
    c.execute("INSERT INTO programming VALUES('Python',3.6, 'Beginner')")
    c.execute("INSERT INTO programming VALUES('Python',2.7, 'Advanced')")
    c.execute("INSERT INTO programming VALUES('Python',2.6, 'Basic')")
    conn.commit()


def enter_dynamic_data():
    lang = input("What language? ")
    version = float(input("What version? "))
    skill = input("What skill level? ")
    c.execute("INSERT INTO example (Language, Version, Skill) VALUES (?, ?, ?)", (lang, version, skill))
    conn.commit()

def read_from_db():
    sql = "SELECT * FROM programming"
    for row in c.execute(sql):
        print(row)
        #print(type(row))
        print(row[0])


#create_table()
#enter_data()
read_from_db()

conn.close()