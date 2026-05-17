import pytest
from src.parser import extract_repo_path

def test_extract_repo_path_clean_url():
    url = "https://github.com/facebook/react"
    assert extract_repo_path(url) == "facebook/react"

def test_extract_repo_path_messy_url():
    url = "  https:  //github.com/microsoft/vscode/  "
    assert extract_repo_path(url) == "microsoft/vscode"

def test_extract_repo_path_no_https():
    url = "github.com/torvalds/linux"
    assert extract_repo_path(url) == 'torvalds/linux'

