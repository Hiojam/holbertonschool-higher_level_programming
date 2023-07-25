#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, it is safe from MySQL injections!
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get command line argument
    search_name = sys.argv[1]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user="username",
                         passwd="password",
                         db="database")

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Use the escape_string method to
    # sanitize the input and prevent SQL injection
    sanitized_name = MySQLdb.escape_string(search_name)

    # Execute the SQL query to select states matching the sanitized input
    query = "SELECT * FROM states WHERE name \
    LIKE BINARY '{}' ORDER BY id ASC".format(sanitized_name)

    cursor.execute(query)

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
