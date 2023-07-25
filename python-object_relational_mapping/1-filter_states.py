#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa, but takes the state name as an
argument from the command line.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to select states
    # with names starting with the given input
    cursor.execute("SELECT * FROM states WHERE name \
                   LIKE BINARY %s ORDER BY id ASC", (state_name,))

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
