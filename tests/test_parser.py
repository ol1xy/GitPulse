import pytest
from src.parser import extract_repo_path

@pytest.mark.parametrize("input_url, expected", [
    ("https://github.com/facebook/react", "facebook/react"),
    ("https://github.com/facebook/react/", "facebook/react"),
    ("github.com/facebook/react", "facebook/react"),
    ("  https://github.com/facebook/react/issues/123 ", "facebook/react"),
    ("http://github.com/facebook/react", "facebook/react"),
    ("facebook/react", "facebook/react"),
    ("http://github.com/facebook/react.git", "facebook/react"),


])
def test_extract_repo_path_valid_inputs(input_url, expected):
    """
    Test that valid URLs and strings are correctly parsed into 'owner/repo'.
    """

    result = extract_repo_path(input_url)
    assert result == expected


@pytest.mark.parametrize("invalid_url", [
    "https://github.com/facebook",
    "facebook",
    "",
    "   /   ",
    "https://github.com/facebook.react"
])
def test_extract_repo_path_invalid_inputs(invalid_url):
    """
    Test that invalid inputs correctly raise a ValueError.
    """
    
    with pytest.raises(ValueError, match="Invalid GitHub URL provided"):
        extract_repo_path(invalid_url)