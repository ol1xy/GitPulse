import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")

BASE_URL = "https://api.github.com"
HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api_Version": "2022-11-28"
}

def fetch_basic_repo_info(repo_path: str) -> dict:
    """
    Fetches basic repository vitals: stars, forks, and open issues.
    """
    url = f"{BASE_URL}/repos/{repo_path}"
    response = requests.get(url, headers = HEADERS)

    if response.status_code == 404:
        raise Exception("Repository not found (404). Check the URL.")
    elif response.status_code == 401 or response.status_code == 403:
        raise Exception("API Rate limit exceeded or Invalid Token (401/403).")
    
    if response.status_code == 200:
        data = response.json()
    
        community_url = f"{url}/community/profile"
        community_response = requests.get(community_url, headers=HEADERS)

        community_files = {
            "has_readme": False,
            "has_license": False,
            "has_contributing": False,
            "has_coc": False
        }

        if community_response.status_code == 200:
            community_data = community_response.json()
            community_files = {
                "has_readme": bool(community_data.get("readme")),
                "has_license": bool(community_data.get("license")),
                "has_contributing": bool(community_data.get("contributing")),
                "has_coc": bool(community_data.get("code_of_conduct"))
            }

        repo_vitals = {
            "name": data.get("full_name"),
            "stars": data.get("stargazers_count"),
            "forks": data.get("forks_count"),
            "open_issues": data.get("open_issues_count"),
            "last_pushed": data.get("pushed_at"),
            "community": community_files
        }

        return repo_vitals
    
    raise Exception(f"Unexpected error: {response.status_code}")

if __name__ == "__main__":
    try:
        info = fetch_basic_repo_info("facebook/react")
        print("Sucesfully fetched data:")
        print(info)
    except Exception as e:
        print(f"Error occured: {e}")