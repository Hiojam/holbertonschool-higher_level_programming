import sys
import MySQLdb


def list_cities_by_state(mysql_user, mysql_password, database_name):
    try:
        # Connect to MySQL server running on localhost at port 3306
        connection = MySQLdb.connect(
            host='localhost', port=3306,
            user=mysql_user, passwd=mysql_password,
            db=database_name
        )

        # Create a cursor to interact with the database
        cursor = connection.cursor()

        # Execute the query to retrieve cities with their respective states
        query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id ASC;
        """
        cursor.execute(query)

        # Fetch and display the results
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    # Check if the script is executed with the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python 4-cities_by_state.py \
            <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Get the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Call the function to list cities by state
    list_cities_by_state(mysql_username, mysql_password, database_name)
