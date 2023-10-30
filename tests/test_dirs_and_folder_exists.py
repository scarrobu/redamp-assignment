"""
Testing if files and folder exists
"""
import os
import pytest

    # directories
@pytest.mark.parametrize('dirs', [
    os.path.exists('../data_sources/'),
    os.path.exists('../data_download/'),
])

@pytest.mark.skip(reason='Can be used after "main.py load" command')
def test_sources_directory_exist(dirs):
    """
    Test if data_sources and data_download folder exists, can by used (disable @pytest.mark.skip)
    after use "main.py load" command.
    """
    path = dirs
    assert path is True

    # data files
@pytest.mark.parametrize('files', [
    os.path.exists('../data_download/urlhaus.abuse.ch.txt'),
    os.path.exists('../data_download/reputation.txt'),
    os.path.exists('../data_download/feed.txt'),
    os.path.exists('../data_sources/data_sources.txt')])

@pytest.mark.skip(reason='Can be used after "main.py load" command')
def test_text_file_exist(files):
    """
    Test if data_download folder contains files, can by used (disable @pytest.mark.skip)
    after use "main.py load" command.
    """
    path = files
    assert path is True
