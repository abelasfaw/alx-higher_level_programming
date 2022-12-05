#!/usr/bin/python3
''' takes in the name of a state as an argument and lists all cities of
that state'''


import sys
import MySQLdb as mdb


if __name__ == '__main__':
    db = mdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `cities` INNER JOIN `states` ON\
                `cities`.`state_id` = `states`.`id` ORDER BY `cities`.`id`")
    first_result = True
    for city in cur.fetchall():
        if city[4] == sys.argv[4]:
            if (first_result):
                print(city[2], end="")
                first_result = False
            else:
                print(", {}".format(city[2]), end="")
    print()
