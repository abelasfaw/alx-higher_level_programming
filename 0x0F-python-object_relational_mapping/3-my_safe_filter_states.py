#!/usr/bin/python3
'''displays all values in the states table of hbtn_0e_0_usa where
name matches the argument provided and is safe from sql injection'''


import sys
import MySQLdb as mdb


if __name__ == '__main__':
    db = mdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    for state in cur.fetchall():
        if (state[1] == sys.argv[4]):
            print(state)
