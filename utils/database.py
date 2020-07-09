import os

import mysql.connector as connentor
from dotenv import load_dotenv

load_dotenv()

def select(table,lines,criterion:str = None) -> str:
    connect = connentor.connect(user=os.getenv('user'),database=os.getenv('database'),passwd=os.getenv('passwd'),host=os.getenv('host'))
    cursor = connect.cursor()
    what_in_database = ""
    for row in lines:
        if what_in_database == "":
            what_in_database += f"`{str(row)}`"
        else:
            what_in_database += f", `{str(row)}`"
    if criterion != None:
        send = f"SELECT {what_in_database} FROM {table} WHERE {criterion}"
    else:
        send = f"SELECT {what_in_database} FROM {table}"
    cursor.execute(send)
    result = cursor.fetchall()
    connect.commit()
    return result
def insert(table,lines,values):
    connect = connentor.connect(user=os.getenv('user'),database=os.getenv('database'),passwd=os.getenv('passwd'),host=os.getenv('host'))
    cursor = connect.cursor()
    what_in_database = ""
    for row in lines:
        if what_in_database == "":
            what_in_database += f"`{str(row)}`"
        else:
            what_in_database += f", `{str(row)}`"
    values_in_database = ""
    for row in values:
        if values_in_database == "":
            values_in_database += f"'{str(row)}'"
        else:
            values_in_database += f", '{str(row)}'"
    send = f"INSERT INTO {table} ({what_in_database}) VALUES ({values_in_database})"
    cursor.execute(send)
    connect.commit()

def update(table,column:str,value:str,criterion):
    connect = connentor.connect(user=os.getenv('user'),database=os.getenv('database'),passwd=os.getenv('passwd'),host=os.getenv('host'))
    cursor = connect.cursor()
    column_in_database = ""
    for i in range(len(column)):
        if column_in_database == "":
            column_in_database += f"{column[i]} = '{value[i]}'"
        else:
            column_in_database += f",\n{column[i]} = '{value[i]}'"
    send = f"""UPDATE {table}
            SET {column_in_database}
            WHERE {criterion}
            """
    cursor.execute(send)
    connect.commit()

def delete(table,where):
    connect = connentor.connect(user=os.getenv('user'),database=os.getenv('database'),passwd=os.getenv('passwd'),host=os.getenv('host'))
    cursor = connect.cursor()
    send = f"DELETE FROM {table} WHERE {where}"
    cursor.execute(send)
    connect.commit()