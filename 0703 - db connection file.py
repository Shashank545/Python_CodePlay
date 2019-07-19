import MySQLdb

def connection():
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='cookies',
                           db='EpicDB')
    c = conn.cursor()

    return c, conn


if __name__ == '__main__':
    c, conn = connection()
    print('it worked!')
