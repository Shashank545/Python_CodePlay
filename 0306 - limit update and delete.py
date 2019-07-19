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


def read_from_database():
    sql = "SELECT * FROM example"
    for row in c.execute(sql):
        print(row)

    print(20*"#")

    sql = "UPDATE example SET Language = 'Python' WHERE Language = 'Java'"
    c.execute(sql)

    sql = "SELECT * FROM example"
    for row in c.execute(sql):
        print(row)

    print(20*"@")
    sql = "DELETE FROM example WHERE Skill = 'Expert'"
    c.execute(sql)

    sql = "SELECT * FROM example"
    for row in c.execute(sql):
        print(row)

read_from_database()

conn.close()
