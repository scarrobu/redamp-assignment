"""
Functions for handling opening on disk and downloading files from web pages.
"""
import os
import requests

# load urls from souces list and save them in to data_download folder
def load_data():
    """
    Downloads data from specified URLs and saves them to files on disk.
    """
    if not os.path.exists('data_download'):
        os.mkdir('data_download')

    try:
        with open('data_sources/data_sources.txt', 'r', encoding='utf-8') as file_data:
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

            print("All files was downloaded successfully, insert data in to DB with (main.py fill)")

    except FileNotFoundError:
        print('ERROR: Folder "data_sources" or file "data_sources.txt" does not exists!')
        print('       Folder was created for you.')
        print('       Please provide file "data_sources.txt" with correct data (links of pages).')
        if not os.path.exists('data_sources'):
            os.mkdir('data_sources')

# open downloaded file one by one, parse desired data and store them in variable
def open_file(path):
    """
    Open a text file at the specified path, extracts the data, returns a list of URLs, IP addresses.
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
