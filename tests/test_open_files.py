"""
Testing the function to open files
"""
import pytest
from ..functions import open_file

@pytest.mark.parametrize('open_files', [
    open_file('../data_download/urlhaus.abuse.ch.txt'),
    open_file('../data_download/reputation.txt'),
    open_file('../data_download/feed.txt'),
])

    # open file
@pytest.mark.skip('Can be used after "main.py load" command')
def test_open_data_file(open_files):
    """
    test if files has lenght an its data type, can by used (disable @pytest.mark.skip)
    after use "main.py load" command.
    """
    data = open_files
    assert isinstance(data, list)
    assert len(data) > 0
