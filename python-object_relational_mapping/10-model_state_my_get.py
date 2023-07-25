#!/usr/bin/python3
"""
Prints the State object with the name passed
as an argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    if len(sys.argv) < 5:
        print("Usage: python 10-model_state_my_get.py <mysql_username> \
              <mysql_password><database_name> <state_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(mysql_username, mysql_password,
                                  database_name), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the State object with the specified state_name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the result or 'Not found'
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
