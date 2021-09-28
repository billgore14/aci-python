import connection as c
import mysql.connector
from colorama import Fore, Style


# read user from table
def readUserInfo():
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        for column in cursor:
            print(Fore.MAGENTA, f'''
            id .............. {column[0]}
            First Name ...... {column[1]}
            Last Name ....... {column[2]}
            Age ............. {column[3]}
            Phone ........... {column[4]}
            ''')
        print(Style.RESET_ALL)
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from my MySQL', error)


# inserts user data into table


def insertUserInfo(fname, lname, age, phone):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO users (user_firstname, user_lastname, user_age, user_phone) VALUES ('{fname}', '{lname}', {age} , '{phone}')")
        conn.commit()
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from my MySQL', error)

# deletes user from table


def deleteUser(id):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM users WHERE user_id = {id}')
        conn.commit()
        readUserInfo()
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from my MySQL', error)
