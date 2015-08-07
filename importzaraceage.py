import csv

import sqlite3

with sqlite3.connect("zagenderrace.db") as connection:
    cursor = connection.cursor()

    ages = csv.reader(open("ZAMaleWhite.csv", "rU"))
    try:
        cursor.execute("CREATE TABLE population('age' TEXT, '2002' INT, '2003' INT, '2004' INT, '2005' INT, \
            '2006' INT, '2007' INT, '2008' INT, '2009' INT, '2010' INT, '2011' INT, '2012' INT, '2013' INT, '2014' INT)")
    except:
        pass

    cursor.executemany("INSERT INTO population('age', '2002', '2003', '2004', '2005', \
                       '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014') \
                       values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", ages)
