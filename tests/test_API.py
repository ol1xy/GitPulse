import pytest
from unittest.mock import patch, MagicMock
from src.api import fetch_basic_repo_info

def create_mock_response(status_code, json_data):
    mock_resp = MagicMock()
    mock_resp.status_code = status_code
    mock_resp.json.return_value = json_data
    return mock_resp

@patch('src.api.requests.get')
def test_fetch_basic_repo_info_all_success(mock_get):
    """
    Happy Path: All returns code 200
    """

    resp_base = create_mock_response(200, {
        "full_name": "facebook/react",
        "stargazers_count": 200000,
        "forks_count": 40000,
        "open_issues_count": 1000,
        "pushed_at": "2023-10-25T10:00:00Z"
    })
    
    resp_community = create_mock_response(200, {
        "readme": {"url": "..."},
        "license": {"name": "MIT"},
        "contributing": {"url": "..."},
        "code_of_conduct": None 
    })
    
    resp_commits = create_mock_response(200, [
        {
            "commit": {
                "message": "Fix critical bug",
                "author": {"name": "John Doe", "date": "2023-10-25T10:00:00Z"}
            }
        }
    ])

    mock_get.side_effect = [resp_base, resp_community, resp_commits]


    result = fetch_basic_repo_info("facebook/react")

    assert result["name"] == "facebook/react"
    assert result["community"]["has_readme"] is True
    assert result["community"]["has_coc"] is False
    assert result["latest_commit"]["author"] == "John Doe"
    
    assert mock_get.call_count == 3


@patch('src.api.requests.get')
def test_fetch_basic_repo_info_partial_failure(mock_get):
    """
    Edge Case: Basic information is available, but there is no community profile (404), and the repository is empty (no commits, 409).
    The function MUST NOT crash; it should return empty values..
    """
    resp_base = create_mock_response(200, {"full_name": "empty/repo", "stargazers_count": 0})
    resp_community = create_mock_response(404, {})
    resp_commits = create_mock_response(409, {})

    mock_get.side_effect = [resp_base, resp_community, resp_commits]

    result = fetch_basic_repo_info("empty/repo")

    assert result["name"] == "empty/repo"
    assert result["community"]["has_readme"] is False
    assert result["latest_commit"] == {}

@patch('src.api.requests.get')
def test_fetch_basic_repo_info_not_found(mock_get):
    """
    Negative Test: First request to repository returns 404.
    """
    mock_get.return_value = create_mock_response(404, {})

    with pytest.raises(Exception, match="Repository not found"):
        fetch_basic_repo_info("invalid/repo")
        
    assert mock_get.call_count == 1