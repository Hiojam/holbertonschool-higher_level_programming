#!/usr/bin/python3
"""Change the name of a State object from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    if len(sys.argv) < 4:
        print("Usage: python 12-model_state_update_id_2.py \
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

    # Get the State object with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    if state_to_update:
        # Update the name of the State object
        state_to_update.name = "New Mexico"

        # Commit the changes to the database
        session.commit()

    # Close the session
    session.close()
