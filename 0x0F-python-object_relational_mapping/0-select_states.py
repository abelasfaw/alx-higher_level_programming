#!/usr/bin/python3
''' lists all states from the database hbtn_0e_0_usa where results
are sorted by state id'''


import sys
import MySQLdb as mdb


if __name__ == "__main__":
    db = mdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id')
    for state in cur.fetchall():
        print(state)
