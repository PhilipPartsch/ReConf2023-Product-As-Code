# use it with: pytest -s test_gitlink.py
import sys
import os
sys.path.append(os.path.abspath('.'))
import gitlink
import pytest
from pathlib import Path

def test_pytest_pass():
    repo_dir = Path().resolve()
    my_repo = gitlink.find_repo(repo_dir)
    print('got repo: ' + str(my_repo))
    my_url = gitlink.get_base_url_from_repo(my_repo)
    print('got base url: ' + str(my_url))
    my_hoster = gitlink.get_hoster_from_url(my_url)
    print('got git hoster: ' + str(my_hoster))
    my_edit_url = gitlink.get_edit_url_from_folder(repo_dir)
    print('got git hoster edit url: ' + str(my_edit_url))
    assert True
