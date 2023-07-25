#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class definition of a State"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    if len(sys.argv) < 4:
        print("Usage: python model_state.py <mysql_username>\
            <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        mysql_username, mysql_password,
        database_name), pool_pre_ping=True)

    # Create all the tables in the database
    # (in this case, just the 'states' table)
    Base.metadata.create_all(engine)
