'''
Python ke sath mysql database connection:

MYSQL database ko python ke sath connect karne ke liye 3 parameter chaiye hain:

1. host (server): localhost
2. user: root
3. password: ''

Yaad rahe abhi hum kewal mysql server ko python ke sath me connect kar rahe hain.

Issi liye yaha par kewal 3 arguments hi pass kiye gaye hain connect() method me.

Jab hum apna database create kar lenge then hum 4th agrument connect method ke andar pass karnege.

Jo ki hamare database ka name hoga. Like as ki hum database ka name denge - heysushil_python
'''

# import mysql connection libary to finally connetct mysql with python.
import mysql.connector as con

mydb = con.connect(host='localhost', user='root', password='', database='heysushil_python')

# print('\n', mydb)
