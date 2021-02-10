import os

import mysql.connector as connentor
from dotenv import load_dotenv

load_dotenv()

def connection():
     conn = connentor.connect(
        user=os.getenv('user'),
        database=os.getenv('database'),
        passwd=os.getenv('passwd'),
        host=os.getenv('host'))
     return (conn,conn.cursor())

def commitWith(conn,cursor,f=lambda:true):
    cursor.execute(send)
    result = f()
    connection.commit()
    return result

def listKeysValues(keys:str,values:str) -> str :
    show_pair = lambda kv: f"{kv[0]} = '{kv[1]}'"
    return (',\n').join(map(show_pair, zip(keys,values)))

def select(table,lines,criterion:str = None) -> str:
    connect, cursor = connection()
    show_elem = lambda x: f"`{x}`"
    
    db_content = (,).join(map(show_elem,lines))
    
    if criterion != None:
        send = f"SELECT {db_content} FROM {table} WHERE {criterion}"
    else:
        send = f"SELECT {db_content} FROM {table}"
    return commitWith(cursor,connect,lambda:cursor.fetchall())

def insert(table,lines,values):
    connect, cursor = connection()
    
    show_elem = lambda x: f"`{x}`"
    
    db_content = (,).join(map(show_elem,lines))
    db_values = (,).join(map(show_elem,values))

    send = f"INSERT INTO {table} ({db_content}) VALUES ({db_values})"
    
    commitWith(cursor,connect)

def update(table,column:str,value:str,criterion):
    connect, cursor = connection()
    
    send = f"""UPDATE {table}
            SET {listKeysValues(column,value)}
            WHERE {criterion}
            """
    commitWith(cursor,connect)

def delete(table,where):
    connect, cursor = connection()
    send = f"DELETE FROM {table} WHERE {where}"
    commitWith(cursor,connect)
