import csv
import MySQLdb

connection = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="", db="")
cursor = connection.cursor()

QueryCheck ='''DROP TABLE IF EXISTS ECTMAY2020; 
               CREATE TABLE ECTMAY2020(SN int, name varchar(255), contribution varchar(255))'''
cursor.execute(QueryCheck)
#USING dictreader to print values 
with open(r'C:\Users\Admin\Desktop\Java\Tasks\EctMay2020.csv') as csv_fileRead:
    reader = csv.DictReader(csv_fileRead, delimiter = ',')
    for line in reader:
        print(line['SN'], line['Name'], line['Contribution'])

        # insert into MYsql as Table
        connection = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="", db="")
        insert_statement = "INSERT INTO ECTMAY2020(SN ,name, contribution) VALUES (%s,%s,%s)"
        connect = connection.cursor()
        connect.executemany(insert_statement,[(line['SN'], line['Name'], line['Contribution'])])
        connection.escape_string(insert_statement)
        connection.commit()