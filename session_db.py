from create_db import get_session, DataSource, IPAddress, URL
from functions import open_file


session = get_session()


def fill_db():
    # takes lines from .txt and create list names form this lines
    with open('data_sources/data_sources.txt', "r") as f:
        data_sources = []
        for line in f:
            data_sources.append(line.strip())

    # for each element of list use one row in database on table data_sources
    for source_name in data_sources:
        data_source = DataSource(name=source_name)
        session.add(data_source)
    session.commit()
    
    # for each cleaned data in file use one row in database on table ip_addresses
    data_ip = open_file('data_download/reputation.txt')
    for ip in data_ip:
        ip_address = IPAddress(address=ip, source_id=1) # mark source as nr. 1 from data_sources list
        session.add(ip_address)
    session.commit()

    # for each cleaned data in file use one row in database on table urls
    data_url = open_file('data_download/urlhaus.abuse.ch.txt')
    for url in data_url:
        url_adress = URL(url=url, source_id=2) # mark source as nr. 2 from data_sources list
        session.add(url_adress)
    session.commit()

    # for each cleaned data in file use one row in database on table urls
    data_url = open_file('data_download/feed.txt')
    for url in data_url:
        url_adress = URL(url=url, source_id=3) # mark source as nr. 3 from data_sources list
        session.add(url_adress)
    session.commit()
