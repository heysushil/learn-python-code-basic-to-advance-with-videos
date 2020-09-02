'''
Important points in MySQLi

1. create:
    a. Database: CREATE DATABASE yourDatabaseName
    b. Table: CREATE TABLE yourTableName(define table columns)
2. Insert:
    a: Value ko table me insert karne ke liye table column name and column par jane wali values
    b: Query: INSERT INTO TABLE tableName(columeName) VALUES(yourValues)
3. Select:
    a: * : SELECT * FROM tableName
    b: column wise: SELECT columnName1, columnName2 FROM tableName
    c: WHERE: SELECT * FROM tableName WHERE columnName=youValue
    d: LIKE: SELECT * FROM tableName WHERE columnName LIKE '%yourTerm%'
    e: ORDER BY: SELECT * FROM tableName ORDER BY columName DESC/ASC
    f: DELETE: DELETE FROM tableName WHERE columnName=yourData
    g: UPDATE: UPDATE tableName SET columnName=yourData WHERE columnName=yourData
    h: LIMIT: SELECT * FROM tableName LIMIT 10
4. TABLE JOIN:
    a. INNER JOIN
    b. LEFT JOIN
    c. RIGHT JOIN    
5. DROP TABLE/DATABASE
    a. TABLE: DROP TABLE tabelName
    b. DATABASE: DROP DATABASE databaseName    

Ye jarui topics hain padh lena:

1. About mysql?
2. How many mysql keys?
3. How many types of table joining and there work behaviour?
'''