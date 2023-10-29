"""
Main file, usage:

Start with:
        main.py init  --  to create db
        main.py load  --  to download data from web sources
        main.py fill  --  to fill DB with transformed data

After this, your database file is filled with data.
"""
import sys

from functions import load_data, open_file
from create_db import create_db
from session_db import fill_db


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'init':
            create_db()
        elif sys.argv[1] == 'load':
            load_data()
        elif sys.argv[1] == 'fill':
            open_file('d')
            fill_db()
        else:
            print('Unknown argument, please use only: init|load|fill.')

    else:
        print(__doc__)
