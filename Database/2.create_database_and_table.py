'''
Create database by python:

Hamesa yad rahe ki sql ki query me jo keyword pre-define hain unko capital letter me hi likhna. 

Baki user define keywords ko jaise caho waise likh sakte ho. Means capital ya small letter me.

Yaad rehe ki database create karne ke turant baad usko connect me as a 4th parameter pass karna jaruri hai.

Database me use hone wale important datatypes:

1. VARCHAR: Ye number, aplhabets, special char sabhi ko accept karta hain.
2. INT: Ye interger number ko accept karta hai.
3. Float: Ye folat number ko accept karta hai.
4. DATETIME: Ye date time formate me date ya time ko store karta hai.

Iske alwa bhi bahot sare datatypes hain aur in sabhi datatypes ke single valeu ko store karne ki alag-alag capacity hain.

MySQL database ki querys ko likhte time syntax ka dhyan rakhe
'''

import installing_and_connecting_db as con

print('\n', con.mydb)

# Get cursor form mydb varaibel which is holding database connection
mycursor = con.mydb.cursor()

# Finally going to create database
# for handling database error use IF NOT EXISTS
mycursor.execute('CREATE DATABASE IF NOT EXISTS heysushil_python')

# create table in our database
# sr / goods_name / price / dates / person
mycursor.execute('CREATE TABLE IF NOT EXISTS aug_month(sr INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, goods_name VARCHAR(250), price INT(8), dates VARCHAR(12), person VARCHAR(100))')
