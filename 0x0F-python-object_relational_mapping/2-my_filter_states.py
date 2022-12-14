#!/usr/bin/python3
''' lists all states whose name matches arugment provided'''


import sys
import MySQLdb as mdb


if __name__ == "__main__":
    db = mdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` WHERE BINARY `name`='{}' ORDER BY `id`"
                .format(sys.argv[4]))
    for state in cur.fetchall():
        print(state)
