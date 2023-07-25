#!/usr/bin/python3
"""Adds the State object "Louisiana" to the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    if len(sys.argv) < 4:
        print("Usage: python 11-model_state_insert.py \
              <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(mysql_username, mysql_password,
                                  database_name), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Create the State object for "Louisiana"
    new_state = State(name="Louisiana")

    # Add the new State object to the session
    session.add(new_state)

    # Commit the changes to the database
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close the session
    session.close()
