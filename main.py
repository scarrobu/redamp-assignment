import sys

from functions import load_data, open_file
from create_db import create_db
from session_db import fill_db


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = 'data/'
        if sys.argv[1] == 'init':
            create_db() 
            print("Your database was created successfully, continue with downloading data (main.py load)")
        elif sys.argv[1] == 'load':
            load_data()
            print("Files from data_sources.txt was downloaded successfully, continue with inserting data to DB (main.py fill)")
        elif sys.argv[1] == 'fill':
            open_file(path)   
            fill_db()
            print("Databases was successfully filled with data from sources, your DB is ready.")

    else:
        print("usage:\nStart with:\n\tmain.py init  --  to create db\n\tmain.py load  --  to download data from web sources\n\tmain.py fill  --  to fill DB with transformed data")
