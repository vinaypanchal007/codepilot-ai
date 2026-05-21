import os

from ingestion.clone_repos import (
    clone_repository
)

from ingestion.read_files import (
    read_files
)

from ingestion.config import (
    REPOSITORIES,
    BASE_DIR
)

def main():
    print("Starting  respository ingestion process...")
    
    for repo in REPOSITORIES:
        repo = repo.strip()
        clone_repository(repo)
        repo_path = os.path.join(BASE_DIR, repo)
        files = read_files(repo_path)
    
    print("Repository ingestion process completed.")
    
if __name__ == "__main__":
    main()