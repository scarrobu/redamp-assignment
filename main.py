"""
Main file, usage:
    Start with:
            main.py load  --  to download data from web sources
            main.py fill  --  to create empty DB file and fill it with transformed data
    After this, your database file is ready to examine.
"""
import sys

from functions import load_data
from session_db import fill_db


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'load':
            load_data()
        elif sys.argv[1] == 'fill':
            fill_db()
        else:
            print('Unknown argument, please use only: load|fill.')

    else:
        print(__doc__)
