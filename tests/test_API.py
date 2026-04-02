import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}

target_repo = "facebook/react"
url = f"https://api.github.com/repos/{target_repo}"

response = requests.get(url, headers=HEADERS)

if response.status_code == 200:
    data = response.json()
    print(f"Project Name: {data['name']}")
    print(f"Stars: {data['stargazers_count']}")
    print(f"Forks: {data['forks_count']}")
else:
    print(f"Error: {response.status_code}")