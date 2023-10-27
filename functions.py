import os
import requests

# load urls from souces list and save them in to data_download folder
def load_data():
    with open('data_sources/data_sources.txt', 'r') as f: # data_sources file with sources links
        for line in f:
            source_url = line.strip()
            response = requests.get(source_url)

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
    _, file = os.path.split(path)
    
    urladdress = []
    if file == 'urlhaus.abuse.ch.txt':
        with open(path, 'r') as f:
            for _ in range(9): # skip fist 9 lines because the file start with some info and header
                next(f)
            for line in f:
                elements = line.split(',') # data are separated by ','
                urladdress.append(elements[2])
            return urladdress
    
    ipaddress = []
    if file == 'reputation.txt':
        with open(path, 'r') as f:
            for line in f:
                elements = line.split('#') # data are separated by '#'
                ipaddress.append(elements[0])
            return ipaddress


    if file == 'feed.txt':
        with open(path, 'r') as f:
            for line in f:
                urladdress.append('"'+line.strip()+'"') # no need to separate data, one line = one link
            return urladdress



