import sqlite3

CREATE_TABLE = "CREATE TABLE IF NOT EXISTS times (id INTEGER PRIMARY KEY, name STRING, time FLOAT, event STRING);"
ADD_TIMES = "INSERT INTO times (name, time, event) VALUES (?,?,?);"
GET_TIMES = "SELECT * FROM times;"
CLEAR_TIMES = "DELETE FROM times;"
GET_BEST_TIME = "SELECT * FROM times WHERE event = ? ORDER BY time ASC LIMIT 1;"
GET_WORST_TIME = "SELECT * FROM times WHERE event = ? ORDER BY DESC LIMIT 1;"

def connect():
    return sqlite3.connect("data.db")

def create_table(connection):
    with connection:
        connection.execute(CREATE_TABLE)
    
def add_time(connection,name, time, event):
    with connection:
        connection.execute(ADD_TIMES,(name,time,event))

def get_times(connection):
    with connection:
        return connection.execute(GET_TIMES).fetchall()

def clear_database(connection):
    with connection:
        connection.execute(CLEAR_TIMES)

def get_best_time(connection, event):
    with connection:
        return connection.execute(GET_BEST_TIME, (event,)).fetchone()
    
def get_worst_time(connection, event):
    with connection:
        return connection.execute(GET_WORST_TIME, (event,)).fetchone()