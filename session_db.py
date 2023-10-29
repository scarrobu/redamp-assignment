"""
This file handling:
    - get_session from create_db.py.
    - iterate trough data_sources.txt and.
    - added data to every table in database.
    - commit all data after adding.
"""
from create_db import get_session, DataSource, IPAddress, URL
from functions import open_file


def fill_db():
    """
    Populates a database with data from text file.
        - 'data_sources' populated with names read from the 'data_sources.txt'.
        - 'ip_addresses' filled with IP addresses from the 'reputation.txt', with source ID 1.
        - 'urls' filled with URLs from 'urlhaus.abuse.ch.txt' and 'feed.txt', with source IDs 2, 3.
    """
    session = get_session()
    error = 0
    # takes lines from .txt and create list names form this lines
    try:
        with open('data_sources/data_sources.txt', "r", encoding="utf-8") as f_var:
            data_sources = []
            for line in f_var:
                data_sources.append(line.strip())

        # for each element of list use one row in database on table data_sources
        for source_name in data_sources:
            data_source = DataSource(name=source_name)
            session.add(data_source)
        session.commit()
    except FileNotFoundError:
        error += 1
        print('ERROR: File "data_sources.txt" has not found in "data_souces/"')

    # for each cleaned data in file use one row in database on table ip_addresses
    try:
        data_ip = open_file('data_download/reputation.txt')
        for ip_iter in data_ip:
            ip_address = IPAddress(address=ip_iter, source_id=1) #mark source as 1 from sources list
            session.add(ip_address)
        session.commit()
    except FileNotFoundError:
        error += 1
        print('ERROR: File "reputation.txt" has not found in "data_download/"')

    # for each cleaned data in file use one row in database on table urls
    try:
        data_url = open_file('data_download/urlhaus.abuse.ch.txt')
        for url in data_url:
            url_adress = URL(url=url, source_id=2) # mark source as nr. 2 from data_sources list
            session.add(url_adress)
        session.commit()
    except FileNotFoundError:
        error += 1
        print('ERROR: File "urlhaus.abuse.ch.txt" has not found in "data_download/"')

    # for each cleaned data in file use one row in database on table urls
    try:
        data_url = open_file('data_download/feed.txt')
        for url in data_url:
            url_adress = URL(url=url, source_id=3) # mark source as nr. 3 from data_sources list
            session.add(url_adress)
        session.commit()
    except FileNotFoundError:
        error += 1
        print('ERROR: File "feed.txt" has not found in "data_download/"')

    if error == 0:
        print("Databases was successfully filled with data from sources, your DB is ready.")
    else:
        print("Databases was successfully created only with data where you dont get error.")
        print('You have ', error, ' errors.')
