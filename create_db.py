from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

# classes for tables in database
class DataSource(Base):
    __tablename__ = 'data_sources'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class IPAddress(Base):
    __tablename__ = 'ip_addresses'
    id = Column(Integer, primary_key=True)
    address = Column(String)
    source_id = Column(Integer, ForeignKey('data_sources.id'))

class URL(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    source_id = Column(Integer, ForeignKey('data_sources.id'))


# create new database
def create_db():
    # engine uses sqlite but can be replaced by postrges, see comment on next line
    engine = create_engine('sqlite:///malicious_IOC.db', echo=False) # postgresql://[username]:[password]@localhost/[db_name]
    Base.metadata.drop_all(bind=engine, tables=[DataSource.__table__, IPAddress.__table__, URL.__table__]) # drop table if exists
    Base.metadata.create_all(engine)

    return engine

# used in session_db to fill database
def get_session():

    Session = sessionmaker(bind=create_db().engine)
    session = Session()

    return session
    