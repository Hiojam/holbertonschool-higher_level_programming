#!/usr/bin/python3
"""
Script that creates a new table "cities"
in the database and populates it with data.
"""

import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user="username",
                         passwd="password",
                         db="database")

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    try:
        # Create the "cities" table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cities (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                state_id INT NOT NULL,
                FOREIGN KEY (state_id) REFERENCES states(id)
            )
        """)

        # Sample data to populate the "cities" table
        cities_data = [
            ("City A", 1),  # City A belongs to state with id 1
            ("City B", 1),  # City B belongs to state with id 1
            ("City C", 2),  # City C belongs to state with id 2
            ("City D", 2),  # City D belongs to state with id 2
            ("City E", 3),  # City E belongs to state with id 3
        ]

        # Insert data into the "cities" table
        cursor.executemany("INSERT INTO cities (name, state_id)\
            VALUES (%s, %s)", cities_data)

        # Commit the changes to the database
        db.commit()

        print("Table 'cities' created and data populated successfully!")

    except Exception as e:
        # Rollback the changes if an error occurs
        db.rollback()
        print("Error:", e)

    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()
