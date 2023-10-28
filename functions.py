"""
PLACEHOLDER
"""
import os
import requests

# load urls from souces list and save them in to data_download folder
def load_data():
    """
    PLACEHOLDER
    """
    with open('data_sources/data_sources.txt', 'r', encoding='utf-8') as file_data: # data_sources
        for line in file_data:
            source_url = line.strip()
            response = requests.get(source_url, timeout=3)
            print('Opening ' + str(source_url) + ' status code: ' + str(response.status_code))

            if source_url == 'https://urlhaus.abuse.ch/downloads/csv_recent':
                with open("data_download/urlhaus.abuse.ch.txt", "wb") as file:
                    file.write(response.content)

            if source_url == 'https://reputation.alienvault.com/reputation.data':
                with open("data_download/reputation.txt", "wb") as file:
                    file.write(response.content)

            if source_url == 'https://openphish.com/feed.txt':
                with open("data_download/feed.txt", "wb") as file:
                    file.write(response.content)

# open downloaded file one by one, parse desired data and store them in variable
def open_file(path):
    """
    PLACEHOLDER
    """
    _, file = os.path.split(path)

    urladdress = []
    ipaddress = []

    if file == 'urlhaus.abuse.ch.txt':
        with open(path, 'r', encoding='utf-8') as file_data:
            print('Open ', file)
            for _ in range(9): # skip fist 9 lines because the file start with some info and header
                next(file_data)
            for line in file_data:
                elements = line.split(',') # data are separated by ','
                urladdress.append(elements[2])
            print('Data are extracted')
            return urladdress

    if file == 'reputation.txt':
        with open(path, 'r', encoding='utf-8') as file_data:
            print('Open ', file)
            for line in file_data:
                elements = line.split('#') # data are separated by '#'
                ipaddress.append(elements[0])
            print('Data are extracted')
            return ipaddress

    if file == 'feed.txt':
        with open(path, 'r', encoding='utf-8') as file_data:
            print('Open ', file)
            for line in file_data:
                urladdress.append('"'+line.strip()+'"')
                # no need to separate data, one line == one link
            print('Data are extracted')
            return urladdress
