import sqlite3

schema_query = open('db.sql').read()
with sqlite3.connect('test.db') as conn:
    cursor = conn.cursor()
    cursor.execute(schema_query)
