import mysql.connector
import os
import sys
from mysql.connector import Error
import getopt

# creating sql files
path = "C:\\Users\\hp\\PycharmProjects\\pythonProject2\\lavanya"
if not os.path.exists(path):
    os.makedirs(path, 0o755)
items = ["124 createtable1.sql","047.createtable1.sql","025 createtable1.sql"]
for val in items:
      fname= path +"/" +"{}".format(val)
      with open(fname, "w") as x:
          x.write("INSERT INTO TEST VALUES("1")
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
list_of_files = os.listdir(path)
files = 0
file_values = []
#extracting numbers from filenames
while files < len(list_of_files):
    if any(letters.isspace() for letters in list_of_files[files]):
        result = (list_of_files[files]). split(' ')
        file_values.append(result[0])
    else:
        result =(list_of_files[files]).split('.')
        file_values.append(result[0])
    files += 1


set(file_values)
integer_map = map(int, file_values)
integer_list_files = list(integer_map)
max_value = max(integer_list_files)
#print(file_values)
#print(max_value)
# updating the Table
if max_value > versions[0]:
    #print(file_values)
    for words in file_values:
        mycursor.execute("UPDATE versiontable SET versions = %s" % words)
else:
    pass
mycursor.execute("SELECT * FROM versiontable")
print(mycursor.fetchall())

