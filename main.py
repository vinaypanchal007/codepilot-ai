import os
import git
from dotenv import load_dotenv

load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")

REPOSITORIES = os.getenv("REPOSITORIES").split(",")

BASE_DIR = "./repos"
os.makedirs(BASE_DIR, exist_ok=True)

def clone_repository(repo_name):
    repo_url = f"https://github.com/{GITHUB_USERNAME}/{repo_name}"
    repo_path = os.path.join(
        BASE_DIR,
        repo_name
    )
    if os.path.exists(repo_path):
        print(f"{repo_name} already exists")
        return
    git.Repo.clone_from(
        repo_url,
        repo_path
    )
    print(f"{repo_name} cloned successfully")

for repo in REPOSITORIES:
    clone_repository(repo)