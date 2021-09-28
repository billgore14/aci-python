import mysql.connector
import os
from mysql.connector import connect


def returnConnection():
    conn = connect(
        host="mydatabase.cle2y1qwvs7w.us-east-1.rds.amazonaws.com",
        user="admin",
        password="pass1976",
        database="myDB"
    )
    return conn
