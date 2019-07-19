import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")

def enter_data():
    c.execute("INSERT INTO example VALUES('Python', 2.7, 'Beginner')")
    c.execute("INSERT INTO example VALUES('Python', 3.3, 'Intermediate')")
    c.execute("INSERT INTO example VALUES('Python', 3.4, 'Expert')")
    conn.commit()

def enter_dynamic_data():
    lang = input("What language? ")
    version = float(input("What version? "))
    skill = input("What skill level? ")

    c.execute("INSERT INTO example (Language, Version, Skill) VALUES (?, ?, ?)", (lang, version, skill))

    conn.commit()
    

enter_dynamic_data()

conn.close()
