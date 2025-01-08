import sqlite3



CREATE_TABLE = "CREATE TABLE IF NOT EXISTS times (id PRIMARY KEY, name STRING, time FLOAT, event STRING);"
ADD_TIMES = "INSERT INTO times (name, time, event) VALUES (?,?,?);"
GET_TIMES = "SELECT name,time FROM times;"
CLEAR_TIMES = "DELETE FROM times;"
GET_BEST_TIME = "SELECT name, time FROM times WHERE event = ? ORDER BY time ASC LIMIT 1;"
GET_WORST_TIME = "SELECT name, time FROM times WHERE event = ? ORDER BY DESC LIMIT 1;"
GET_SORTED_TIMES_EVENT = "SELECT name, time FROM times WHERE event = ? order by time ASC"
GET_TIMES_EVENT = "SELECT name, time FROM times WHERE event = ?"

connection = sqlite3.connect("data.db")
c = connection.cursor()

def create_table():
        c.execute(CREATE_TABLE)
    
def add_time(name, time, event):
        c.execute(ADD_TIMES,(name,time,event))

def get_times():
        return (c.execute(GET_TIMES).fetchall())

def clear_database(c):
        c.execute(CLEAR_TIMES)

def get_best_time(event):
        return c.execute(GET_BEST_TIME, (event,)).fetchone()
    
def get_worst_time(event):
        return c.execute(GET_WORST_TIME, (event,)).fetchone()
    
def get_sorted_times_by_event(event):
        return c.execute(GET_SORTED_TIMES_EVENT, (event,)).fetchall()
    
def get_times_per_event(event):
        return (c.execute(GET_TIMES_EVENT, (event,)).fetchall())
def get_average_time(event):
        table = (c.execute(GET_TIMES_EVENT, (event,)).fetchall())
        sum = 0
        for row in table:
                sum += row[1]
        return sum/len(table)
