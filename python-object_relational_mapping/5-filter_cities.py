import sys
import MySQLdb


def filter_cities_by_state(mysql_user, mysql_password,
                           database_name, state_name):
    try:
        # Connect to MySQL server running on localhost at port 3306
        connection = MySQLdb.connect(
            host='localhost', port=3306,
            user=mysql_user, passwd=mysql_password,
            db=database_name
        )

        # Create a cursor to interact with the database
        cursor = connection.cursor()

        # Prepare the query with a placeholder
        # for the state name to avoid SQL injection
        query = """
            SELECT GROUP_CONCAT(name SEPARATOR ', ')
            FROM cities
            INNER JOIN states
            ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC;
        """

        # Execute the query with the provided
        # state name as a parameter
        cursor.execute(query, (state_name,))

        # Fetch and display the results
        results = cursor.fetchone()
        if results:
            print(results[0])
        else:
            print("State not found in the database.")

        # Close the cursor and connection
        cursor.close()
        connection.close()

    except MySQLdb.Error as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    # Check if the script is executed with the correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: python 5-filter_cities.py <mysql_username>\
            <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    # Get the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to filter cities by state
    filter_cities_by_state(mysql_username, mysql_password,
                           database_name, state_name)
