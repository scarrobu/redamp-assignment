"""
This file contains SQLAlchemy classes data for creating tables and
contains functions for creating table ans retrieving session connection.
"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

# classes for tables in database
class DataSource(Base):
    """
    Class handling data for data souces table
    """
    __tablename__ = 'data_sources'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class IPAddress(Base):
    """
    Class handling data for IP adress table
    """
    __tablename__ = 'ip_addresses'
    id = Column(Integer, primary_key=True)
    address = Column(String)
    source_id = Column(Integer, ForeignKey('data_sources.id'))

class URL(Base):
    """
    Class handling data for URLs table
    """
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    source_id = Column(Integer, ForeignKey('data_sources.id'))

# create new database
def create_db():
    """
    Create database with DataSource, IPAddress and URL tables
    
    Returns:
        SQLAlchemy engine objekt
    """
    # engine uses sqlite but can be replaced by postrges, see comment on the next line
    # postgresql://[username]:[password]@localhost/[db_name]
    engine = create_engine('sqlite:///malicious_IOC.db', echo=False)
    Base.metadata.drop_all(bind=engine, \
                           tables=[DataSource.__table__, IPAddress.__table__, URL.__table__])
    Base.metadata.create_all(engine)

    print("Empty DB file was created successfully, continue with downloading data (main.py load)")
    return engine

# used in session_db to fill database
def get_session():
    """
    Creates and returns session for work with database
    Returns:
        SQLAlchemy session objekt.
    """
    session_instance = sessionmaker(bind=create_db().engine)
    session = session_instance()

    return session
