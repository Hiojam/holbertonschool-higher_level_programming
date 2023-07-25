#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    if len(sys.argv) < 4:
        print("Usage: python 14-model_city_fetch_by_state.py \
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

    # Query all City objects from the database, sorted by cities.id
    cities = session.query(City).order_by(City.id).all()

    # Print the City objects in the desired format
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    # Close the session
    session.close()
