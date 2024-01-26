import mysql.connector

connection = mysql.connector.connect(
    host=ps_host,
    user=ps_user,
    password=ps_password,
    database=ps_database
)

if connection.is_connected():
    print('Connected to the database!')
