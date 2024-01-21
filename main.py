import sqlite3

# Connect to the SQLite database using a context manager
with sqlite3.connect('database.db') as conn:
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute an SQL query to select data
    cursor.execute('SELECT * FROM expenses')  # Replace 'your_table' with the actual table name

    # Fetch all the rows from the query result
    rows = cursor.fetchall()

    # Iterate through the rows and print or process the data
    for row in rows:
        print(row)
