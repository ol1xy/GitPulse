from urllib.parse import urlparse

def extract_repo_path(url: str) -> str:
    """
    Parses a GitHub URL and returns 'owner/repo' string.
    Example:m 'https://github.com/facebook/react/' -> 'facebook/react'
    """

    clean_url = url.strip().strip('/')
    parsed = urlparse(clean_url)

    if not parsed.netloc:
        parts = clean_url.split("/")
    else:
        path = parsed.path.lstrip("/")
        parts = path.split('/')

    if parts and parts[0] == "github.com":
        parts.pop(0)

    if len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    else:
        raise ValueError("Invalid GitHub URL provided")
    
if __name__ == "__main__":
    print(extract_repo_path("https://github.com/ol1xy/GitPulse"))