import mysql.connector
import os
import sys
from mysql.connector import Error
import getopt

# crating Mysql database connection
hst_name, usr_name, password, dbase  = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
try:
    mydb = mysql.connector.connect(
      host=hst_name,
      user=usr_name,
      password=password,
      database=dbase
    )

    mycursor = mydb.cursor()
except Error as e:
    print("error while connecting to MySQL")
# creating and inserting values into table
mycursor.execute("DROP TABLE IF EXISTS versiontable")
#mycursor.execute("DELETE versions FROM versiontable")
mycursor.execute("CREATE TABLE `versiontable` (`versions` INT NOT NULL, PRIMARY KEY (`versions`))")
mycursor.execute("INSERT INTO versiontable VALUES(%s)", (int(25),))
mydb.commit()
mycursor.execute("SELECT * FROM versiontable")
versions =[int(record[0]) for record in mycursor.fetchall()]
#print(versions)
#print(versions[0])