#!/usr/bin/python3
'''lists all cities from the database hbtn_0e_4_usa'''


import sys
import MySQLdb as mdb


if __name__ == '__main__':
    db = mdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT `cities`.`id`, `cities`.`name`, `states`.`name`\
                FROM `cities` INNER JOIN `states` on `cities`.`state_id`\
                = `states` .`id` ORDER BY `cities`.`id`")
    for city in cur.fetchall():
        print(city)
