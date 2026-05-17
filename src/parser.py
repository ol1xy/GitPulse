from urllib.parse import urlparse

def extract_repo_path(url: str) -> str:
    """
    Parses a GitHub URL and returns 'owner/repo' string.
    Example:m 'https://github.com/facebook/react/' -> 'facebook/react'
    """

    clean_url = url.strip().strip('/')
    parsed = urlparse(clean_url)

    path = parsed.path.lstrip("/")
    parts = path.split('/')

    if len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    else:
        return ValueError("Invalid GitHub URL provided")
    
if __name__ == "__main__":
    print(extract_repo_path("https://github.com/ol1xy/GitPulse"))
